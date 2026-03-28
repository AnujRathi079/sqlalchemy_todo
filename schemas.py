from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str
    user_id: int


class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    name: str


class UserResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True