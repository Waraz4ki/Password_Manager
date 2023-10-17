import sqlalchemy
from typing import Any, Optional, List
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
from sqlalchemy import Table, Column, Integer, String, ForeignKey, DATETIME, DATE

metadata_obj = MetaData()
engine = create_engine(f"sqlite:///data/asda.db")

class Base(DeclarativeBase):
    pass

#class Entries(Base):
#    __tablename__ = "Entries"
#    id = Column("id", Integer, primary_key=True)
#    title = Column("title", String())
#    password = Column("password", String())
#    notes =  Column("notes", String())
#    assigned_group = Column("assigned_group", ForeignKey("Groups.id"))
#    date = Column(DATETIME)
#
#class Groups(Base):
#    __tablename__ = "Groups"
#    id = Column("id", Integer, primary_key=True)
#    group_name = Column("group_name", String())
    
class Entry(Base):
    __tablename__ = "Entry"
    
    id : Mapped[int] = mapped_column(primary_key=True)
    title : Mapped[str]
    password : Mapped[str]
    notes : Mapped[str]
    assigned_group = mapped_column(ForeignKey("Group.id"))
    
    def __repr__(self) -> str:
        return f"{self.id}, {self.title}, {self.password}, {self.notes}, {self.assigned_group}"
    
class Group(Base):
    __tablename__ = "Group"
    
    id : Mapped[int] = mapped_column(primary_key=True)
    group_name : Mapped[str]
    
    def __rep__(self) -> str:
        return f"{self.id}, {self.group_name}"


#? Use this to create all the defined tables al a 'class ...(Base):'
#! Must use Subclass of DeclarativeBase like above, see: sqlalchemy.exc.InvalidRequestError: Cannot use "DeclarativeBase" directly as a declarative base class. Create a Base by creating a subclass of it
asd = Entry()
Base.metadata.create_all(engine)
