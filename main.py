from fastapi import FastAPI, Depends, HTTPException, status, Path
from models import Base, Todos
from typing import Annotated
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import schemas
from routers import auth


app = FastAPI()

Base.metadata.create_all(bind = engine)


app.include_router(auth.router) 

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()



db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/", status_code = status.HTTP_200_OK, response_model = list[schemas.TodoResponse])
async def read_all(db: db_dependency):
    return db.query(Todos).all()

@app.get("/todo/{todo_id}")
async def read_todo( db: db_dependency, todo_id: int = Path(gt = 0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if not todo_model:
        raise HTTPException(status_code=404, detail = f"Task with id = {todo_id} not found")
    return todo_model
 
@app.post("/todo", status_code=status.HTTP_201_CREATED, response_model=schemas.TodoResponse)
async def create_todo(db: db_dependency, todo_request: schemas.TodoRequest):
    todo_model = Todos(**todo_request.model_dump())

    db.add(todo_model)
    db.commit()

    return todo_model


@app.put("/todo/edit/{todo_id}", response_model = schemas.TodoResponse)
async def edit_todo(db: db_dependency, todo_id: int, content: schemas.TodoUpdate):
    todo_model_ref = db.query(Todos).filter(Todos.id == todo_id)
    todo_model_instance = todo_model_ref.first()

    if not todo_model_instance:
        raise HTTPException(status_code=404, detail = f"Task with id = {todo_id} not found")

    update_fields = content.model_dump(exclude_unset=True)
    todo_model_ref.update(values = update_fields, synchronize_session=False) # type: ignore
    db.commit()


    update_todo = db.query(Todos).filter(Todos.id == todo_id).first()
    return update_todo
    

@app.delete("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def delete_todo(db: db_dependency, todo_id: int):
    todo_model_ref = db.query(Todos).filter(Todos.id == todo_id)
    todo_model_instance = todo_model_ref.first()

    if not todo_model_instance:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Task with id = {todo_id} not found")

    todo_model_ref.delete(synchronize_session=False)
    db.commit()

    
    


    