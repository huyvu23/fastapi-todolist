from pydantic import BaseModel

class TodoBase(BaseModel):
    """
    Base model for a Todo item.

    Attributes:
        title (str): The title of the Todo item.
        completed (bool): The completion status of the Todo item. Defaults to False.
    """
    title: str
    completed: bool = False

class TodoCreate(TodoBase):
    """
    Schema for creating a new Todo item.

    Inherits from TodoBase and does not add any additional fields.
    This class is used for validation and serialization of the data
    required to create a new Todo item.
    """
    pass

class Todo(TodoBase):
    id: int
