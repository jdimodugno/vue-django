import graphene

from backend.api import (
    schema,
)

class Mutations(schema.Mutations, graphene.ObjectType):
    pass

class Query(schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutations)
