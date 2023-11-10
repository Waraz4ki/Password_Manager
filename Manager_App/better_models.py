from . import db

from typing import Any, Optional, List
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class Database(db.Model):
    __tablename__ = "database"
    
    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str]
    master_key : Mapped[str] = mapped_column(nullable=False)
    
    #contained_groups : Mapped[Optional[List["Group"]]] = relationship(back_populates="assigned_database")
    
    def is_authenticated():
        pass


class Group(db.Model):
    __tablename__ = "group"
    
    id : Mapped[int] = mapped_column(primary_key=True)
    group_name : Mapped[Optional[str]]
    
    assigned_database_id : Mapped[Optional[int]] = mapped_column(ForeignKey("database.id"))
    #assigned_database : Mapped["Database"] = relationship(back_populates="contained_groups")
    
    #contained_entries : Mapped[Optional[List["Entry"]]] = relationship(back_populates="assigned_group")

    def __rep__(self) -> str:
        return f"{self.id}, {self.group_name}"


class Entry(db.Model):
    __tablename__ = "entry"

    id : Mapped[int] = mapped_column(primary_key=True)
    title : Mapped[Optional[str]]
    name : Mapped[Optional[str]]
    password : Mapped[Optional[str]]
    url : Mapped[Optional[str]]
    
    assigned_group_id : Mapped[Optional[int]] = mapped_column(ForeignKey("group.id"))
    #assigned_group : Mapped["Group"] = relationship(back_populates="contained_groups")
    
    def __repr__(self) -> str:
        return f"{self.id}, {self.title}, {self.name}, {self.password}, {self.url}"
