from django.conf.urls import url

from .views import (
    beer_resource,
    rating_resource,
    user_resource,
)


urlpatterns = (
    url(
        'beers',
        beer_resource,
        name="beer_resource"
    ),
    url(
        'beer-ratings',
        rating_resource,
        name="rating_resource"
    ),
    url(
        'users',
        user_resource,
        name="user_resource"
    ),

)
