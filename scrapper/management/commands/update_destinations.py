import os
from urllib.error import HTTPError

from django.core.files import File
from django.core.management.base import BaseCommand

from destination.models import Destination
from scrapper.models import Selector
from scrapper.utils import (get_agency_destination_urls, get_destination_data,
                            get_destination_picture, get_num_of_nights,
                            get_picture, get_price, get_title)


class Command(BaseCommand):

    help = "Update destinations in database."

    def handle(self, *args, **kwargs):
        for selector in Selector.objects.all():
            for destination in Destination.objects.filter(selector_url=selector.offers_url):
                destination.image.delete()
                destination.delete()

            destination_urls = get_agency_destination_urls(selector)
            prices = get_price(selector)
            num_of_nights = get_num_of_nights(selector)
            pictures = get_destination_picture(selector)
            titles = get_title(selector)

            for url in destination_urls:
                destination_data = get_destination_data(
                    selector.agency.url + url,
                    selector
                )

                if not Destination.objects.filter(original_url=url):
                    destination = Destination.objects.create(
                        name=titles[url],
                        original_url=url,
                        description=destination_data,
                        price=prices[url],
                        agency=selector.agency,
                        num_of_nights=int(num_of_nights[url]),
                        selector_url=selector.offers_url
                    )
                    image_name = destination.name.split(' ')[0].replace(',', '') + '.jpg'
                    try:
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
                    except HTTPError:
                        pass
