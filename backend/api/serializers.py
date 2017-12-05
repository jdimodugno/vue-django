from django.conf import settings

from django.contrib.auth.models import User
from backend.models import Beer, Rating
from rest_framework import serializers
from rest_framework.authtoken.models import Token


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'token')

    def get_token(self, user):
        token = Token.objects.get_or_create(user=user)[0]
        return token.key


# Serializers define the API representation.
class BeerSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    score = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Beer
        fields = ('description', 'abv', 'name', 'id', 'image_url', 'score')

    def get_name(self, beer):
        if beer.name:
            return beer.name

        return beer.brand.name

    def get_image_url(self, beer):
        if beer.image:
            return settings.MEDIA_ROOT + beer.image.url
        else:
            return ""

    def get_score(self, beer):
        return beer.score


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('__all__')
