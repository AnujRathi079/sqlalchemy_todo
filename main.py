from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models, database, crud, schemas

# Create tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


# Dependency (DB session)
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user.name)


@app.post("/tasks", response_model=schemas.TodoResponse)
def create_task(task: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task.title, task.user_id)


@app.get("/users/{user_id}/tasks", response_model=list[schemas.TodoResponse])
def get_user_tasks(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_tasks(db, user_id)