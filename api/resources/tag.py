from api import Resource, abort, reqparse, auth
from api.models.tag import TagModel
from api.schemas.tag import tag_schema, tags_schema
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, use_kwargs, doc
from api.schemas.tag import TagSchema, TagRequestSchema
from api import db


# parameters:
# 1. path
# 2. body
# 3. query
@doc(tags=['Tags'])
class TagResource(MethodResource):
    @doc(summary="Get tag by id", description="Returns tag")
    @doc(responses={404: {"description": 'Tag not found'}})
    @marshal_with(TagSchema, code=200)
    def get(self, tag_id):
        tag = TagModel.query.get(tag_id)
        if tag is None:
            abort(404, error=f"Tag with id={tag_id} not found")
        return tag, 200

    @auth.login_required(role="admin")
    @doc(description='Edit tag by id')
    @marshal_with(TagSchema)
    @doc(security=[{"basicAuth": []}])
    def put(self, tag_id):
        parser = reqparse.RequestParser()
        parser.add_argument("tag_name", required=True)
        tag_data = parser.parse_args()
        tag = TagModel.query.get(tag_id)
        tag.name = tag_data["tag_name"]
        tag.save()
        return tag, 200

    # @auth.login_required
    def delete(self, tag_id):
        raise NotImplemented  # не реализовано!


@doc(tags=['Tags'])
class TagsListResource(MethodResource):
    @marshal_with(TagSchema(many=True), code=200)
    def get(self):
        tags = TagModel.query.all()
        return tags, 200

    @doc(summary="Create new Tag", description="Подробное описание метода POST")
    @use_kwargs(TagRequestSchema, location='json')
    # @use.kwargs({"name": fields.String()}, location='json')    # в нашем случае наша схема десериализации очень простая, поэтому вместо строки выше можно использовать это, но мы оставим вариант выше (он лучше, так как позволяет легко изменять схему десериализации, особенно в больших проектах)
    @marshal_with(TagSchema, code=201)
    def post(self, **kwargs):
        tag = TagModel(**kwargs)
        db.session.add(tag)
        db.session.commit()
        return tag, 201

# Сериализация: obj --> dict --> str
# Десериализация: str --> dict --> obj
