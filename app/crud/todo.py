from app.schemas.todo import TodoCreate
from app.models.todo import Todo
from app.core.storage import todos

def create_todo(todo_create: TodoCreate) -> Todo:
    new_id = len(todos) + 1
    todo = Todo(
        id=new_id,
        title=todo_create.title,
        description=todo_create.description
    )
    todos.append(todo)
    return todo

def get_all_todos():
    return todos