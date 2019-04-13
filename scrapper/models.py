from django.db import models

from agency.models import Agency


class Selector(models.Model):
    """
    Define css selectors and url needed for getting data.
    """
    offers_url = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    agency = models.OneToOneField(Agency, on_delete=models.CASCADE)
    travel_plan = models.CharField(max_length=100, blank=True)
    price_includes = models.CharField(max_length=100, blank=True)
    price_excludes = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    image_gallery = models.CharField(max_length=100, blank=True)
