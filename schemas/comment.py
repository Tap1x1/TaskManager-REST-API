from ma import ma
from models.comment import CommentModel
from models.task import TaskModel


class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CommentModel
        load_only = ("task",)
        dump_only = ("id",)
        include_fk = True
        load_instance = True