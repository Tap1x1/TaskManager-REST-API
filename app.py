import os

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_uploads import configure_uploads
from marshmallow import ValidationError

from db import db
from ma import ma

from views.project import Project, ProjectList
from views.task import Task, TaskList, CloseTask
from views.comment import Comment
from views.user import UserRegister, User, UserLogin
from views.file import FileUpload, File
from libs.file_helper import FILE_SET


app = Flask(__name__)
load_dotenv(".env", verbose=True)
# SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
# SQLALCHEMY_TRACK_MODIFICATIONS = False
app.config['UPLOADED_FILES_DEST'] = os.path.join("static", "file")
configure_uploads(app, FILE_SET)
app.secret_key = 'fdjgkfdjkgjdfkgj'
app.config.from_object("default_config")
app.config.from_envvar("APPLICATION_SETTINGS")
api = Api(app)
jwt = JWTManager(app)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


api.add_resource(UserRegister, "/api/register")
api.add_resource(User, "/api/user/<int:user_id>")
api.add_resource(UserLogin, "/api/login")
api.add_resource(Project, "/api/project/<string:name>")
api.add_resource(ProjectList, "/api/projects")
api.add_resource(Task, "/api/task/task_name=<string:name>")
api.add_resource(CloseTask, "/api/close-task/<int:id>")
api.add_resource(TaskList, "/api/tasks")
api.add_resource(Comment, "/api/task_id=<int:task_id>/comment/")
api.add_resource(FileUpload, "/api/task/upload/file")
api.add_resource(File, "/api/task/file/<int:user_id>")


if __name__ == '__main__':
    ma.init_app(app)
    app.run(host='0.0.0.0')
