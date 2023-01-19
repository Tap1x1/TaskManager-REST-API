from datetime import datetime
from typing import List
from models.user import UserModel

from db import db


class TaskModel(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(250))
    status = db.Column(db.String(80), nullable=False, default="True")
    created_data = db.Column(db.DateTime(), default=datetime.now)
    closed_data = db.Column(db.DateTime())
    user_created_task = db.Column(db.String(80))
    user_assigment_task = db.Column(db.String(80), db.ForeignKey("users.username"), nullable=False)
    user_model = db.relationship("UserModel")
    comments = db.relationship("CommentModel", lazy="dynamic")
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"), nullable=False)
    project = db.relationship("ProjectModel")
    file_list = db.Column(db.String(180), default="none")

    @classmethod
    def find_by_id(cls, _id: int) -> "TaskModel":
        return cls.query.filter_by(id=_id).first()

    # @classmethod
    # def find_by_user_created_task(cls, name: str) -> "TaskModel":
    #     return cls.query.filter_by()

    @classmethod
    def find_by_name(cls, name: str) -> "TaskModel":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls) -> List["TaskModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

