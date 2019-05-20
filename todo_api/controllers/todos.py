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


def find_todos_by_id(todo_id):
    """ Find a todo task by id in DB """
    todo = Todos.query.get(todo_id)

    if todo is not None:
        todo_schema = TodosSchema()
        return {'todo': todo_schema.dump(todo).data}, 200
    else:
        return {'error': 'Todo task not found for ID: {todo_id}'.format(todo_id=todo_id)}


def update_todos_by_id():
    pass


def delete_todos_by_id():
    pass
