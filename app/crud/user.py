from app.schemas.user import UserBase
from app.models.user import User
from app.core.storage import users

def register_user(user:UserBase):
    new_id = len(users) + 1
    new_user = User(
        id=new_id,
        username=user.username,
        password=user.password,
    )
    users.append(new_user)
    return new_user