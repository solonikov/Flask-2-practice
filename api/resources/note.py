from api import auth, abort, Resource, reqparse
from api.models.note import NoteModel
from api.schemas.note import note_schema, notes_schema


class NoteResource(Resource):
    @auth.login_required
    def get(self, note_id):
        """
        Пользователь может получить ТОЛЬКО свою заметку
        """
        author = auth.current_user()
        note = NoteModel.query.get(note_id)
        if not note:
            abort(404, error=f"Note with id={note_id} not found")
        return note_schema.dump(note), 200

    @auth.login_required
    def put(self, note_id):
        """
        Пользователь может редактировать ТОЛЬКО свои заметки
        """
        author = auth.current_user()
        parser = reqparse.RequestParser()
        parser.add_argument("text", required=True)
        parser.add_argument("private", type=bool)
        note_data = parser.parse_args()
        note = NoteModel.query.get(note_id)
        if not note:
            abort(404, error=f"note {note_id} not found")
        if note.author != author:
            abort(403, error=f"Forbidden")
        note.text = note_data["text"]

        note.private = note_data.get("private") or note.private

        note.save()
        return note_schema.dump(note), 200

    def delete(self, note_id):
        """
        Пользователь может удалять ТОЛЬКО свои заметки
        """
        note = NoteModel.query.get(note_id)
        if not note:
            abort(404, error=f"Note with id={note_id} not found")
        note.delete()
        return "", 204


class NotesListResource(Resource):
    def get(self):
        notes = NoteModel.query.all()
        return notes_schema.dump(notes), 200

    @auth.login_required
    def post(self):
        author = auth.current_user()
        parser = reqparse.RequestParser()
        parser.add_argument("text", required=True)
        parser.add_argument("private", type=bool, required=True)
        note_data = parser.parse_args()
        note = NoteModel(author_id=author.id, **note_data)
        note.save()
        return note_schema.dump(note), 201
