from database import Base
from sqlalchemy import ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(50), unique=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    hashed_password : Mapped[str] = mapped_column(String(100))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    role: Mapped[str] = mapped_column(String(50))

class Todos(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index = True)
    title: Mapped[str]= mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(100))
    priority: Mapped[int] = mapped_column(Integer)
    complete: Mapped[Optional[bool]] = mapped_column(Boolean , default = False)

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))