from pydantic import BaseModel,Field

class UserBase(BaseModel):
    username:str = Field(min_length=5,max_length=100)
    password:str = Field(min_length=5,max_length=100)

# Nó kế thừa toàn bộ thuộc tính và phương thức từ class UserBase.
# Từ khóa pass có nghĩa là "không làm gì cả" – tức là UserCreate không thêm gì mới so với UserBase.
class UserCreate(UserBase):
    pass