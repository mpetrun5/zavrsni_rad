from django.db import models

from agency.models import Agency


class Selector(models.Model):
    """
    Define css selectors and url needed for getting data.
    """
    agency = models.OneToOneField(Agency, on_delete=models.CASCADE)
    offers_url = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)

    title = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    num_of_nights = models.CharField(max_length=100)
    travel_plan = models.CharField(max_length=100)
    image_gallery = models.CharField(max_length=100, blank=True)
