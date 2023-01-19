from db import db


class CommentModel(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(80), nullable=False)
    text = db.Column(db.String(250))
    task_id = db.Column(db.Integer, db.ForeignKey("tasks.id"), nullable=False)
    task = db.relationship("TaskModel")

    @classmethod
    def find_by_task_id(cls, task_id: str) -> "TaskModel":
        return cls.query.filter_by(task_id=task_id).all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()