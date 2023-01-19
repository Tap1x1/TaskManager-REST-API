from ma import ma
from models.task import TaskModel
from schemas.comment import CommentSchema
from schemas.file import FileSchema


class TaskSchema(ma.SQLAlchemyAutoSchema):
    comments = ma.Nested(CommentSchema, many=True)
    files = ma.Nested(FileSchema, many=True)

    class Meta:
        model = TaskModel
        load_only = ("project", "user_model")
        dump_only = ("id",)
        include_fk = True
        load_instance = True