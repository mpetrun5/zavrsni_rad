from django.db import models


class Agency(models.Model):
    """
    Defines agency that is providing data about destinations.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.url
