from ma import ma
from models.user import UserModel
from schemas.task import TaskSchema


class UserSchema(ma.SQLAlchemyAutoSchema):
    user_tasks = ma.Nested(TaskSchema, many=True)

    class Meta:
        model = UserModel
        load_only = ("password",)
        dump_only = ("id",)
        include_fk = True
        load_instance = True