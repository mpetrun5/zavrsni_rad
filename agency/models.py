from django.db import models

from scrapper.models import Selector


class Agency(models.Model):
    """
    Defines agency that is providing data about destinations.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    selector = models.OneToOneField(Selector, on_delete=models.CASCADE)
