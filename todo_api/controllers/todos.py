from todo_api.models.Todos import Todos, TodosSchema


def find_todos():
    """ Fetch and return the list of all todo task """
    todos = Todos.query.order_by(Todos.id).all()
    todo_schema = TodosSchema(many=True)
    todos_docs = todo_schema.dump(todos).data

    result = {'todos': todos_docs}

    return result, 200


def create_todos(body):
    pass


def find_todos_by_id(id):
    pass


def update_todos_by_id():
    pass


def delete_todos_by_id():
    pass
