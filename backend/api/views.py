from .viewsets import (
    BeerViewSet,
    RatingViewSet,
    UserViewSet,
)

user_resource = UserViewSet.as_view({
    'post': 'login',
})

beer_resource = BeerViewSet.as_view({
    'get': 'list',
})

rating_resource = RatingViewSet.as_view({
    'post': 'create',
    'get': 'list',    
})
