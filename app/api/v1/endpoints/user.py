from fastapi import APIRouter,HTTPException
from app.schemas.user import UserCreate,UserBase
from app.crud.user import register_user as add_new_user

router = APIRouter()

@router.post('/', response_model=UserBase)
def create(user:UserCreate):
    try:
        new_user =  add_new_user(user)
        if bool(new_user):
            return new_user
        raise HTTPException(status_code=500, detail="Sign up failed")
    except ValueError as e:
        print("Lỗi:", e)