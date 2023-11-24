from models import Person, engine, Session


def create_person(name: str, age: int):
    person_model = Person(name=name, age=age)

    with Session(engine) as session:
        session.add(person_model)
        session.commit()
        session.refresh(person_model)

    return person_model
