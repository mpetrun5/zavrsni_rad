from django.db import models

from agency.models import Agency


class Destination(models.Model):
    """
    Defines a destination with all its information.
    """
    name = models.CharField(max_length=50)
    agency = models.ForeignKey(Agency, on_delete=models.DO_NOTHING)
    original_url = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    num_of_nights = models.PositiveIntegerField()
    selector_url = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name

    def agency_to_string(self):
        """
        Represent agency field as string for use with elasticsearch index.
        """
        return self.agency.name


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
