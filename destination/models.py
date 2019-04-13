from django.db import models


class Destination(models.Model):
    """
    Defines a destination with all its information.
    """
    name = models.CharField(max_length=50)
    original_url = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    price_indcludes = models.TextField()
    price_excludes = models.TextField()
    num_of_nights = models.PositiveIntegerField()
    is_active = models.BooleanField()
    start_date = models.DateField()


class Country(models.Model):
    name = models.CharField(max_length=100)


class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=50)
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)


class DailyOffer(models.Model):
    """
    Defines a description of a daily offer from destination.
    """
    destination = models.ForeignKey(Destination, on_delete=models.DO_NOTHING)
    date = models.DateField()
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
