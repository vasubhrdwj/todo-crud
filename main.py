from fastapi import FastAPI, Depends, HTTPException, status, Path
from models import Base, Todos
from typing import Annotated
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import schemas
from routers import auth, todos


app = FastAPI()

Base.metadata.create_all(bind = engine)


app.include_router(auth.router) 
app.include_router(todos.router)

