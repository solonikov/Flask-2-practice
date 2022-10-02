import sqlite3
import json
import click

from api import db
from api.schemas.user import UserRequestSchema
from config import Config

from api.models.note import NoteModel
from api.models.user import UserModel

# from sqlalchemy.exc import IntegrityError


# with open(path_to_fixture, "r", encoding="UTF-8") as f:
#     users_data = UserRequestSchema(many=True).loads(f.read())
#     for user_data in users_data:
#         user = UserModel(**user_data)
#         db.session.add(user)
#     db.session.commit()
#     print(f"{len(users_data)} users created")

@click.command
# @click.argument('file_name')
@click.option('--fixture', help='fixture file name')
def load_data(fixture):
    with open(Config.PATH_TO_FIXTURES / fixture, "r", encoding="UTF-8") as f:
        file_data = json.load(f)
        model_name = file_data["model"]
        if model_name == "UserModel":
            model = UserModel
        elif model_name == "NoteModel":
            model = NoteModel

        for obj_data in file_data["data"]:
            obj = model(**obj_data)
            db.session.add(obj)
        db.session.commit()

        print(f"{len(file_data['data'])} objects created")

        # users_data = UserRequestSchema(many=True).loads(f.read())
        # n = 0
        # for user_data in users_data:
        #     user = UserModel(**user_data)
        #     try:
        #         db.session.add(user)
        #         db.session.commit()
        #         n += 1
        #     except IntegrityError:  # Обработка ошибки "создание пользователя с НЕ уникальным именем"
        #         db.session.rollback()
        # print(f"{n} users created")

# path_to_fixture = "fixtures/notes.json"
# load_data(path_to_fixture)

if __name__ == '__main__':
    load_data()


