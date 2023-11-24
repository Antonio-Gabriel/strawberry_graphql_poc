import strawberry

from fastapi import FastAPI
from typing import Optional, List
from strawberry.fastapi import GraphQLRouter

from models import engine, SQLModel

from resolvers.book.create_book import create_book
from resolvers.person.get_persons import get_persons
from resolvers.person.create_person import create_person
from resolvers.subscriptions.realtime_counter_resolver import realtime_counter_resolver

# Create the database
SQLModel.metadata.create_all(engine)


@strawberry.type
class Book:
    id: Optional[int]
    title: str


@strawberry.type
class Person:
    id: Optional[int]
    name: str
    age: int
    books: Optional[List[Book]]


@strawberry.type
class Query:
    all_persons: list[Person] = strawberry.field(resolver=get_persons)


@strawberry.type
class Mutation:
    create_person: Person = strawberry.mutation(resolver=create_person)
    create_book: Book = strawberry.mutation(resolver=create_book)


@strawberry.type
class Subscription:
    realtime_counter: int = strawberry.subscription(
        resolver=realtime_counter_resolver)


schema = strawberry.Schema(
    query=Query, mutation=Mutation, subscription=Subscription)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
