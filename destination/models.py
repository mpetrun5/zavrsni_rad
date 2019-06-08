from django.db import models
from django.contrib.auth.models import User

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

    def original_url_to_string(self):
        """
        Represent original destination url as string for use with elasticsearch index.
        """
        return ''.join([self.agency.url, self.original_url])


class Review(models.Model):
    """
    Defines review of destination.
    """
    SCORE_CHOICES = zip(range(1, 5), range(1, 5))

    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    destination = models.ForeignKey(Destination, on_delete=models.DO_NOTHING)
    rating = models.PositiveIntegerField(choices=SCORE_CHOICES)
