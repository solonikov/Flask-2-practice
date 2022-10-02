from api import auth, abort, Resource, reqparse
from api.models.note import NoteModel
from api.models.tag import TagModel
from api.schemas.note import NoteSchema, NoteCreateSchema
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, use_kwargs, doc
from webargs import fields
from api import db


@doc(tags=['Notes'])
class NoteResource(MethodResource):
    @auth.login_required
    @doc(summary="Get note by id", security=[{"basicAuth": []}])
    @marshal_with(NoteSchema)
    def get(self, note_id):
        """
        Пользователь может получить ТОЛЬКО свою заметку
        """
        author = auth.current_user()
        note = NoteModel.query.get(note_id)
        if not note:
            abort(404, error=f"Note with id={note_id} not found")
        return note, 200

    @auth.login_required
    @doc(summary="Edit note by id", security=[{"basicAuth": []}])
    @marshal_with(NoteSchema)
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
        return note, 200

    @auth.login_required
    @doc(description='Delete note by id', security=[{"basicAuth": []}])
    @doc(responses={401: {"description": "Not authorization"}})
    @doc(responses={404: {"description": "Not found"}})
    def delete(self, note_id):
        """
        Пользователь может удалять ТОЛЬКО свои заметки
        """
        note = NoteModel.query.get(note_id)
        if not note:
            abort(404, error=f"Note with id={note_id} not found")
        note.delete()
        return "", 204


@doc(tags=['Notes'])
class NotesListResource(MethodResource):
    @doc(summary="Get notes list", security=[{"basicAuth": []}])
    @marshal_with(NoteSchema(many=True), code=200)
    def get(self):
        notes = NoteModel.query.all()
        return notes, 200

    @auth.login_required
    @doc(summary="Create note", security=[{"basicAuth": []}])
    @marshal_with(NoteSchema, code=201)
    @use_kwargs(NoteCreateSchema)
    def post(self, **kwargs):
        author = auth.current_user()
        # parser = reqparse.RequestParser()
        # parser.add_argument("text", required=True)
        # parser.add_argument("private", type=bool, required=True)
        # note_data = parser.parse_args()
        note = NoteModel(author_id=author.id, **kwargs)
        note.save()
        return note, 201


@doc(tags=['Notes'])
class NoteSetTagsResource(MethodResource):
    @doc(summary="Set tags to Note")
    @use_kwargs({"tags_id": fields.List(fields.Int())}, location=('json'))    # здесь мы делаем десериализацию прямо в этой строчке, не создавая схему десериализации (по двум причинам 1. это проще, так как у нас очень простой случай  2. вряд ли в этом месте десериализация когда-то будет меняться)
    @marshal_with(NoteSchema)
    def put(self, note_id, **kwargs):
        note = NoteModel.query.get(note_id)
        if not note:
            abort(404, error=f"note {note_id} not found")
        # TODO: получить все тэги по id одним запросом
        for tag_id in kwargs["tags_id"]:
            tag = TagModel.query.get(tag_id)
            note.tags.append(tag)
        db.session.commit()    # эта реализация с циклом плохая, например при добавлении 10 тэгов к 1 заметке будет выполнено 12 запросов к БД -- очень много, так что надо будет улучшить (можно сделать реализацию из 3 запросов на всю функцию)
        return note, 200
