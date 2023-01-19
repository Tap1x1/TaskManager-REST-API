from flask import session, request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from models.project import ProjectModel
from schemas.project import ProjectSchema
from libs.strings import gettext

project_schema = ProjectSchema()
project_list_schema = ProjectSchema(many=True)


class Project(Resource):
    @classmethod
    @jwt_required()
    def get(cls, name: str):
        project = ProjectModel.find_by_name(name)
        if project:
            return project_schema.dump(project), 200
        return {"message": gettext("project_not_found")}, 404

    @classmethod
    @jwt_required()
    def post(cls, name: str):
        if ProjectModel.find_by_name(name):
            return {"message": gettext("project_name_exists").format(name)}, 400
        project = ProjectModel(name=name)
        try:
            project.save_to_db()
        except:
            return {"message": gettext("project_error_inserting")}, 500
        return project_schema.dump(project), 201

    @classmethod
    @jwt_required()
    def delete(cls, name: str):
        project = ProjectModel.find_by_name(name)
        if project:
            project.delete_from_db()
            return {"message": gettext("project_deleted")}, 200
        return {"message": gettext("project_not_found")}, 404


class ProjectList(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        return {"project": project_list_schema.dump(ProjectModel.find_all())}, 200
