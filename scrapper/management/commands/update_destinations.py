# import requests

from django.core.management.base import BaseCommand

from scrapper.models import Selector
from scrapper.utils import (
    get_agency_destination_urls,
    get_destination_data
)


class Command(BaseCommand):

    help = "Update destinations in database."

    def handle(self, *args, **kwargs):
        for selector in Selector.objects.all():
            destination_urls = get_agency_destination_urls(
                selector.offers_url,
                selector.destination
            )

            for url in destination_urls:
                destination_data = get_destination_data(
                    selector.agency.url + url,
                    selector
                )
