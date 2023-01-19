from flask_restful import Resource
from flask import request, session
from flask_jwt_extended import jwt_required
from models.comment import CommentModel
from views.user import UserLogin
from schemas.comment import CommentSchema
from libs.strings import gettext

comment_schema = CommentSchema()
username = UserLogin
comment_list_schema = CommentSchema(many=True)


class Comment(Resource):
    @classmethod
    @jwt_required()
    def post(cls, task_id:int):
        comment_json = request.get_json()
        if comment_json["author"] == session["username"]:
            comment_json["task_id"] = task_id
            comment = comment_schema.load(comment_json)
        else:
            return {"message": gettext("comment_authorized_user")}
        try:
            comment.save_to_db()
        except:
            return {"message": gettext("comment_error_inserting")}, 500
        return comment_schema.dump(comment), 201
