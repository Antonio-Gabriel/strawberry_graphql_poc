from typing import Optional, List
from sqlmodel import SQLModel, Field, create_engine, select, Session, Relationship

engine = create_engine("sqlite:///database.db")


class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int

    books: List['Book'] = Relationship(back_populates="person")


class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str

    person_id: Optional[int] = Field(default=None, foreign_key="person.id")
    person: Optional[Person] = Relationship(back_populates="books")
