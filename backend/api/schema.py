import graphene

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db.models.aggregates import Avg
from django.conf import settings
from graphene_django.types import DjangoObjectType

from rest_framework.authtoken.models import Token

from backend.models import (
    Beer,
    Brand,
    Rating
)


class UserType(DjangoObjectType):
    class Meta:
        model = User


class TokenType(DjangoObjectType):
    class Meta:
        model = Token


class BeerType(DjangoObjectType):
    score = graphene.String()
    votes = graphene.Int()

    def resolve_name(instance, args):
        if not instance.name:
            return instance.brand.name
        return instance.name

    def resolve_image(instance, args):
        if instance.image:
            return settings.MEDIA_ROOT + instance.image.url
        else:
            return ""

    def resolve_score(instance, args):
        return Rating.objects.filter(beer=instance.id).aggregate(Avg('score'))['score__avg']

    def resolve_votes(instance, args):
        return Rating.objects.filter(beer=instance.id).count()

    class Meta:
        model = Beer


class BrandType(DjangoObjectType):
    class Meta:
        model = Brand


class RatingType(DjangoObjectType):
    class Meta:
        model = Rating


class Login(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        password = graphene.String()

    ok = graphene.Boolean()
    user = graphene.Field(lambda: UserType)
    token = graphene.Field(lambda: TokenType)

    def mutate(self, info, username, password):
        user = authenticate(username=username, password=password)
        token = Token.objects.get_or_create(user=user)[0]

        if user and token:
            ok = True

        return Login(user=user, token=token, ok=ok)


class CreateBeerRating(graphene.Mutation):
    class Arguments:
        beer_id = graphene.ID()
        score = graphene.Int()
        user_id = graphene.Int()

    ok = graphene.Boolean()
    rating = graphene.Field(lambda: RatingType)

    def mutate(self, info, beer_id, score, user_id):
        beer = Beer.objects.get(pk=beer_id)
        user = User.objects.get(pk=user_id)
        ok = True
        rating = Rating.objects.create(score=score, beer=beer, user=user)
        return CreateBeerRating(rating=rating, ok=ok)


class Mutations(graphene.ObjectType):
    login = Login.Field()
    create_beer_rating = CreateBeerRating.Field()


class Query(graphene.ObjectType):
    beers = graphene.List(BeerType)
    beer = graphene.Field(BeerType, pk=graphene.ID(), name=graphene.String())

    brands = graphene.List(BrandType)
    brand = graphene.Field(BrandType, pk=graphene.ID(), name=graphene.String())

    ratings = graphene.List(RatingType)

    current_user = graphene.Field(UserType, token=graphene.String())

    def resolve_beers(self, args):
        return Beer.objects.all()

    def resolve_beer(self, info, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')

        if pk:
            return Beer.objects.get(pk=pk)
        elif name:
            return Beer.objects.get(name__iexact=name)
        else:
            return

    def resolve_brands(self, args):
        return Brand.objects.all()

    def resolve_brand(self, info, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')

        if pk:
            return Brand.objects.get(pk=pk)
        elif name:
            return Brand.objects.get(name__iexact=name)
        else:
            return

    def resolve_ratings(self, args):
        return Rating.objects.all()

    def resolve_current_user(self, info, **kwargs):
        token_key = kwargs.get('token')
        return Token.objects.get(key=token_key).user
