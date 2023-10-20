import sqlalchemy
from typing import Any, Optional, List
from sqlalchemy import MetaData, create_engine
from sqlalchemy import insert, update, delete, select
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
#from sqlalchemy import Table, Column, Integer, String, ForeignKey, DATETIME, DATE

metadata_obj = MetaData()
engine = create_engine(f"sqlite:///data/asda.db", echo=True)

class Base(DeclarativeBase):
    pass


class Config(Base):
    __tablename__ = "Config"

    masterKEY : Mapped[str] = mapped_column(primary_key=True)

    def __repr__(self) -> str:
        return f"{self.masterKEY}"    


class Entry(Base):
    __tablename__ = "Entry"

    id : Mapped[int] = mapped_column(primary_key=True)
    title : Mapped[Optional[str]]
    password : Mapped[Optional[str]]
    notes : Mapped[Optional[str]]
    #assigned_group : Mapped["Group"] = relationship(back_populates="assigned_entries")

    def __repr__(self) -> str:
        return f"{self.id}, {self.title}, {self.password}, {self.notes}"


class Group(Base):
    __tablename__ = "Group"
    
    id : Mapped[int] = mapped_column(primary_key=True)
    group_name : Mapped[Optional[str]]
    #assigned_entries : Mapped[Entry] = relationship(back_populates="assigned_group")

    def __rep__(self) -> str:
        return f"{self.id}, {self.group_name}"


if __name__ == "__main__":
    #? Use this to create all the defined tables al a 'class ...(Base):'
    #! Must use Subclass of DeclarativeBase like above, see: sqlalchemy.exc.InvalidRequestError: Cannot use "DeclarativeBase" directly as a declarative base class. Create a Base by creating a subclass of it
    #Base.metadata.create_all(engine, checkfirst=False)
    enter = insert(Entry).values(title="DSB",password="1234")
    get = select(Entry)

    with engine.begin() as be:
        #be.execute(insert(Entry).values(id=1872435))
        be.execute(update(Entry).where(Entry.id==1872435).values(title="Servus", password="1234"))
        #be.execute(enter)
        #print(be.execute(enter).inserted_primary_key)
        #be.execute(get)
