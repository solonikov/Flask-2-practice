from api import ma
from api.models.tag import TagModel

# Сериализация ответа(response)
class TagSchema(ma.SQLAlchemyAutoSchema):
   class Meta:
       model = TagModel
       # fields = ("name",)    # при закомментированной строке при десериализации будут отображены все атрибуты объекта


# Десериализация запроса(request)
class TagRequestSchema(ma.SQLAlchemySchema):
   class Meta:
       model = TagModel

   name = ma.Str()


tag_schema = TagSchema()
tags_schema = TagSchema(many=True)
