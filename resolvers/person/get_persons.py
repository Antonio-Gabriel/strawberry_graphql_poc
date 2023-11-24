from models import Person, engine, select, Session
from sqlalchemy.orm import selectinload


def get_persons() -> list[Person]:
    query = select(Person).distinct().options(selectinload(Person.books))

    with Session(engine) as session:
        result = session.exec(query).fetchall()

    return result
