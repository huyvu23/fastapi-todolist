from fastapi import APIRouter, Depends, HTTPException
from app.schemas.todo import TodoCreate, TodoRead
from app.crud.todo import create_todo, get_all_todos
router = APIRouter()

@router.post("/", response_model=TodoRead)
def create(todo: TodoCreate):
    return create_todo(todo)

@router.get("/", response_model=list[TodoRead])
def read_all():
    return get_all_todos()

