import os

from django.core.files import File
from django.core.management.base import BaseCommand

from destination.models import Destination
from scrapper.models import Selector
from scrapper.utils import (get_agency_destination_urls, get_destination_data,
                            get_destination_picture, get_num_of_nights,
                            get_picture)


class Command(BaseCommand):

    help = "Update destinations in database."

    def handle(self, *args, **kwargs):
        for selector in Selector.objects.all():
            for destination in Destination.objects.filter(agency=selector.agency):
                destination.image.delete()
                destination.delete()

            destination_urls = get_agency_destination_urls(
                selector.offers_url,
                selector.destination
            )
            num_of_nights = get_num_of_nights(
                selector.offers_url,
                selector.destination,
                selector.num_of_nights
            )
            pictures = get_destination_picture(
                selector.offers_url,
                selector.destination
            )

            for url in destination_urls:
                destination_data = get_destination_data(
                    selector.agency.url + url,
                    selector
                )

                if not Destination.objects.filter(name=destination_data['title']):
                    destination = Destination.objects.create(
                        name=destination_data['title'],
                        original_url=url,
                        description=destination_data['description'],
                        price=destination_data['price'],
                        agency=selector.agency,
                        num_of_nights=int(num_of_nights[url]),
                    )
                    image_name = destination.name.split(' ')[0].replace(',', '') + '.jpg'
                    destination.image.save(
                        image_name,
                        File(
                            open(
                                get_picture(image_name, selector.agency.url + pictures[url]),
                                mode='rb',
                            )
                        )
                    )
                    os.remove(get_picture(image_name, selector.agency.url + url))
