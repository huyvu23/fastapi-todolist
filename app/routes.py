from fastapi import APIRouter, HTTPException
from app.schemas import Todo, TodoCreate
from app.models import fake_db

router = APIRouter()

@router.get("/todos", response_model=list[Todo])
def get_todos():
    return fake_db

@router.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo = Todo(id=len(fake_db) + 1, **todo.dict())
    fake_db.append(new_todo)
    return new_todo

@router.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in fake_db:
        if todo.id == todo_id:
            return todo
    #   raise: Từ khóa Python để ném ra (gây ra) một ngoại lệ.
    #   HTTPException: Một lớp ngoại lệ (Exception) được FastAPI cung cấp để trả về các lỗi HTTP cụ thể.
    #   status_code=404: Trả về mã lỗi HTTP 404 Not Found – nghĩa là tài nguyên không tồn tại.
    #   detail="Todo not found": Nội dung thông báo lỗi gửi về cho client (thường ở dạng JSON).
    raise HTTPException(status_code=404, detail="Todo not found")

@router.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated: TodoCreate):
    for i, todo in enumerate(fake_db):
        if todo.id == todo_id:
            new_todo = Todo(id=todo_id, **updated.dict())
            fake_db[i] = new_todo
            return new_todo
    raise HTTPException(status_code=404, detail="Todo not found")

@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, todo in enumerate(fake_db):
        if todo.id == todo_id:
            del fake_db[i]
            return {"message": "Deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")
