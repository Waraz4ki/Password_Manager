import sqlalchemy
from typing import Any, Optional, List
from sqlalchemy import MetaData, create_engine
from sqlalchemy import insert, update, delete, select
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column


metadata_obj = MetaData()
engine = create_engine(f"sqlite:///data/asda.db", echo=True)

class Base(DeclarativeBase):
    pass


class Config(Base):
    __tablename__ = "Config"

    master_key : Mapped[str] = mapped_column(primary_key=True)

    def __repr__(self) -> str:
        return f"{self.master_key}"    


class Entry(Base):
    __tablename__ = "Entry"

    id : Mapped[int] = mapped_column(primary_key=True)
    title : Mapped[Optional[str]]
    name : Mapped[Optional[str]]
    password : Mapped[Optional[str]]
    url : Mapped[Optional[str]]

    def __repr__(self) -> str:
        return f"{self.id}, {self.title}, {self.name}, {self.password}, {self.url}"


class Group(Base):
    __tablename__ = "Group"
    
    id : Mapped[int] = mapped_column(primary_key=True)
    group_name : Mapped[Optional[str]]

    def __rep__(self) -> str:
        return f"{self.id}, {self.group_name}"


if __name__ == "__main__":
    #? Use this to create all the defined tables al a 'class ...(Base):'
    #! Must use Subclass of DeclarativeBase like above, see: sqlalchemy.exc.InvalidRequestError: Cannot use "DeclarativeBase" directly as a declarative base class. Create a Base by creating a subclass of it
    enter = insert(Entry).values(title="DSB",password="1234")
    get = select(Entry).where(Entry.id == 1872435)

    with engine.begin() as be:
        for row in be.execute(get):
            print(row)
        #be.execute(update(Entry).where(Entry.id==1872435).values(title="Servus", password="1234"))
        pass