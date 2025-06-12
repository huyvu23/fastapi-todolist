from fastapi import APIRouter,HTTPException
from app.schemas.todo import TodoCreate, TodoRead
from app.crud.todo import create_todo, get_all_todos,get_todo_according_id
router = APIRouter()

@router.post("/", response_model=TodoRead)
def create(todo: TodoCreate):
    return create_todo(todo)

@router.get("/", response_model=list[TodoRead])
def read_all():
    return get_all_todos()

@router.get("/{id}", response_model=TodoRead)
def get_todo_by_id(id):
    result = get_todo_according_id(int(id))
    if bool(result):
        return result
    raise HTTPException(status_code=404, detail=f"Todo with id {id} not found")

