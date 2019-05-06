from todo_api.models import db


class Todos(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    tittle = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(), nullable=True)
    done = db.Column(db.Boolean, nullable=False)
