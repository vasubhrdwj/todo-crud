from database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

class Todos(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index = True)
    title: Mapped[str]= mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(100))
    priority: Mapped[int] = mapped_column(Integer)
    complete: Mapped[Optional[bool]] = mapped_column(Boolean , default = False)