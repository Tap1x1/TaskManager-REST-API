from ma import ma
from models.project import ProjectModel
from schemas.task import TaskSchema


class ProjectSchema(ma.SQLAlchemyAutoSchema):
    tasks = ma.Nested(TaskSchema, many=True)

    class Meta:
        model = ProjectModel
        dump_only = ("id",)
        load_only = ("id",)
        include_fk = True
        load_instance = True
