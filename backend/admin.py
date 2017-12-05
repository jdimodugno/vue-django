from django.contrib import admin

from .models import (
    Beer,
    Brand,
    Country,
    City,
    Rating,
)

admin.site.register(Beer)
admin.site.register(Brand)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Rating)
