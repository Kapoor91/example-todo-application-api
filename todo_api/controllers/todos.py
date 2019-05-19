from todo_api.models.Todos import Todos, TodosSchema
from todo_api.models import db


def find_todos():
    """ Fetch and return the list of all todo task """
    todos = Todos.query.order_by(Todos.id).all()
    todo_schema = TodosSchema(many=True)
    todos_docs = todo_schema.dump(todos).data

    result = {'todos': todos_docs}

    return result, 200


def create_todos(body):
    """ Create a todo task in DB """
    todo_schema = TodosSchema()
    new_todo = todo_schema.load(body, session=db.session).data

    db.session.add(new_todo)
    db.session.commit()

    return {'todo': todo_schema.dump(new_todo).data}, 201


def find_todos_by_id(id):
    pass


def update_todos_by_id():
    pass


def delete_todos_by_id():
    pass
