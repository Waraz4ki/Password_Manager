from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func
from typing import Any, Optional, List
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column

class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Config(db.Model):
    __tablename__ = "Config"

    master_key : Mapped[str] = mapped_column(primary_key=True)

    def __repr__(self) -> str:
        return f"{self.master_key}"    


class Entry(db.Model):
    __tablename__ = "Entry"

    id : Mapped[int] = mapped_column(primary_key=True)
    title : Mapped[Optional[str]]
    name : Mapped[Optional[str]]
    password : Mapped[Optional[str]]
    url : Mapped[Optional[str]]

    def __repr__(self) -> str:
        return f"{self.id}, {self.title}, {self.name}, {self.password}, {self.url}"


class Group(db.Model):
    __tablename__ = "Group"
    
    id : Mapped[int] = mapped_column(primary_key=True)
    group_name : Mapped[Optional[str]]

    def __rep__(self) -> str:
        return f"{self.id}, {self.group_name}"

