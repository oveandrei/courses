import strawberry
from strawberry.fastapi import GraphQLRouter


# Create a User model
@strawberry.type
class User:
    id: int
    name: str

# Create a Query model
@strawberry.type
class Query:
    user: User = User(id=1, name="Alice")

schema = strawberry.Schema(query=Query) # Create the schema object
graphql_app = GraphQLRouter(schema) 