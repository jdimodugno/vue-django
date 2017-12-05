from django.contrib.auth.models import User
from django.db.models.aggregates import Avg

from rest_framework import viewsets
from rest_framework.permissions import (AllowAny, IsAuthenticated,)
from rest_framework.response import Response

from backend.models import Beer, Rating

from .serializers import (
    UserSerializer,
    BeerSerializer,
    RatingSerializer,
)

from .forms import (
    RatingForm,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

    def login(self, request):
        request_data = request.POST.dict()
        user = None

        try:
            user = User.objects.get(email=request_data['email'])
            if user:
                serializer = self.serializer_class(user)
                return Response(serializer.data, status=200)
        except:
            return Response(status=403)


class BeerViewSet(viewsets.ModelViewSet):
    queryset = Beer.objects.prefetch_related('rating_set').annotate(score=Avg('rating__score')).order_by('score')
    serializer_class = BeerSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticated, )

    def create(self, request):
        data = request.data
        rating_form = RatingForm(data)

        if not rating_form.is_valid():
            return Response(status=408)
        else:
            beer = Beer.objects.get(pk=rating_form.cleaned_data['beer_id'])
            rating = Rating.objects.create(
                score=rating_form.cleaned_data['score'],
                beer=beer,
                user=request.user
            )
            serializer = self.serializer_class(rating)
            return Response(serializer.data)
