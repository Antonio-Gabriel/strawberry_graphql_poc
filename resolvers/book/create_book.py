from models import Book, engine, Session


def create_book(title: str, person_id: int):
    book_model = Book(title=title, person_id=person_id)

    with Session(engine) as session:
        session.add(book_model)
        session.commit()
        session.refresh(book_model)

    return book_model

# import pdb; pdb.set_trace()
# joinedload