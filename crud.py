from sqlalchemy.orm import Session
from models import Todo, User

def create_user(db: Session, name: str):
    user = User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def create_task(db: Session, title: str, user_id: int):
    task = Todo(title=title, user_id=user_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_user_tasks(db: Session, user_id: int):
    return db.query(Todo).filter(Todo.user_id == user_id).all()