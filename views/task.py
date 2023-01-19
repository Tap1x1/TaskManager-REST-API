from datetime import datetime
from flask_restful import Resource
from flask import request, session
from flask_jwt_extended import jwt_required
from models.task import TaskModel
from views.user import UserLogin
from schemas.task import TaskSchema
from libs.strings import gettext


task_schema = TaskSchema()
task_list_schema = TaskSchema(many=True)


class Task(Resource):
    @classmethod
    @jwt_required()
    def get(cls, name: str):
        task = TaskModel.find_by_name(name)
        print(task)
        if task:
            return task_schema.dump(task), 200
        return {"message": gettext("task_not_found")}, 404

    @classmethod
    @jwt_required(fresh=True)
    def post(cls, name: str):
        if TaskModel.find_by_name(name):
            return {"message": gettext("task_name_exists").format(name)}, 400
        task_json = request.get_json()
        task_json["name"] = name
        task_json["user_created_task"] = session['username']
        # task_json["user_assigned_task"] = session['username']
        task = task_schema.load(task_json)
        try:
            task.save_to_db()
        except:
            return {"message": gettext("task_error_inserting")}, 500
        return task_schema.dump(task), 201

    @classmethod
    @jwt_required()
    def delete(cls, name: str):
        task = TaskModel.find_by_name(name)
        if task:
            task.delete_from_db()
            return {"message": gettext("task_deleted")}, 200
        return {"message": gettext("task_not_found")}, 404


class CloseTask(Resource):
    @classmethod
    @jwt_required()
    def post(cls, id: int):
        if TaskModel.find_by_id(id):
            close_task = TaskModel.find_by_id(id)
            close_task.status = False
            close_task.closed_data = datetime.now()
            close_task.save_to_db()
        else:
            return {"message": gettext("task_not_found")}, 404

        return task_schema.dump(close_task), 200


class TaskList(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        return {"tasks": task_list_schema.dump(TaskModel.find_all())}, 200
