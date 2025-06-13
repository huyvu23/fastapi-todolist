from fastapi import APIRouter,HTTPException,status
from fastapi.responses import Response
from app.schemas.todo import TodoCreate, TodoRead
from app.crud.todo import create_todo,delete_todo_item, get_all_todos,get_todo_according_id,update_status_todo
router = APIRouter()

@router.post("/", response_model=TodoRead)
def create(todo: TodoCreate):
    return create_todo(todo)

@router.get("/", response_model=list[TodoRead])
def read_all():
    return get_all_todos()

@router.get("/{id}", response_model=TodoRead)
def get_todo_by_id(id:int):
    try:
        result = get_todo_according_id(int(id))
        if bool(result):
            return result
        raise HTTPException(status_code=404, detail=f"Todo with id {id} not found")
    except ValueError as e:
        print("Lỗi:", e)

@router.put("/{id}")
def update_status_todo_item(id:int,response_model=TodoRead):
    try:
        response = update_status_todo(id)
        if bool(response):
           return response
        raise HTTPException(status_code=404, detail=f"Todo with id {id} not found")
    except ValueError as e:
        print("Lỗi:", e)

@router.delete("/{id}")
def delete_to_by_id(id:int):
    try:
        response = delete_todo_item(id)
        if response:
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        raise HTTPException(status_code=404, detail=f"Todo with id {id} not found")
    except ValueError as e:
        print("Lỗi:", e)



