import sqlalchemy
from typing import Any, Optional, List
from sqlalchemy import MetaData, create_engine, ForeignKey
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


class Group(Base):
    __tablename__ = "Group"
    
    id : Mapped[int] = mapped_column(primary_key=True)
    group_name : Mapped[Optional[str]]
    #entry_id : Mapped[Optional[int]] = mapped_column(ForeignKey("Entry.id"))
    
    assigned_entries : Mapped[Optional[List["Entry"]]] = relationship(backref="Group")

    def __rep__(self) -> str:
        return f"{self.id}, {self.group_name}"


class Entry(Base):
    __tablename__ = "Entry"

    id : Mapped[int] = mapped_column(primary_key=True)
    title : Mapped[Optional[str]]
    name : Mapped[Optional[str]]
    password : Mapped[Optional[str]]
    url : Mapped[Optional[str]]
    
    group_id : Mapped[Optional[int]] = mapped_column(ForeignKey("Group.id"))
    #assigned_group : Mapped["Group"] = relationship(back_populates="assigned_entries")

    def __repr__(self) -> str:
        return f"{self.id}, {self.title}, {self.name}, {self.password}, {self.url}"

if __name__ == "__main__":
    #? Use this to create all the defined tables al a 'class ...(Base):'
    #! Must use Subclass of DeclarativeBase like above, see: sqlalchemy.exc.InvalidRequestError: Cannot use "DeclarativeBase" directly as a declarative base class. Create a Base by creating a subclass of it
    
    
    ent1 = insert(Entry).values(title="DSB", name="Moritz", password="1234", url="21e12sqd2", group_id=1)
    ent2 = insert(Entry).values(title="Youtube", name="Simon", password="4321", url="2837rt2")
    grou1 = insert(Group).values(group_name="First")
    grou2 = insert(Group).values(group_name="Second")
    grou3 = insert(Group).values(group_name="Third")

    #Base.metadata.create_all(engine)
    
    with engine.begin() as be:
        #be.execute(ent1)
        be.execute(select(Entry).where(Entry.title=="DSB")).fetchall()
        