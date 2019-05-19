from todo_api.models import db, ma


class Todos(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(), nullable=False, default='')
    done = db.Column(db.Boolean, nullable=False, default=False)

    def update(self, id=None, title=None, description=None, done=None):
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if done is not None:
            self.done = done


class TodosSchema(ma.ModelSchema):
    class Meta:
        model = Todos
        sqla_session = db.session
    # todo: add url link to access the ressource
