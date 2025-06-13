from fastapi import APIRouter
from app.api.v1.endpoints import todo,user

router = APIRouter()
router.include_router(todo.router, prefix="/todos", tags=["Todos"])
router.include_router(user.router, prefix="/users", tags=["Users"])