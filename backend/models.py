from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


class IntegerRangeField(models.IntegerField):
    def __init__(self,
                 verbose_name=None,
                 name=None,
                 min_value=None,
                 max_value=None,
                 **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


@python_2_unicode_compatible
class Beer(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(max_length=1000)
    abv = models.DecimalField(max_digits=3, decimal_places=2)
    brand = models.ForeignKey('Brand')
    image = models.ImageField(null=True, upload_to='beers')

    def __str__(self):
        if self.name:
            return self.name

        return self.brand.name


@python_2_unicode_compatible
class Brand(models.Model):
    name = models.CharField(max_length=40)
    city = models.ForeignKey('City')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class City(models.Model):
    name = models.CharField(max_length=40)
    country = models.ForeignKey(Country)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Rating(models.Model):
    score = IntegerRangeField(min_value=1, max_value=5)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User)
    beer = models.ForeignKey(Beer)

    def __str__(self):
        return self.beer.name
