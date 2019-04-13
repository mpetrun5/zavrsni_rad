import requests

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = 'Update destinations in database.'

    def handle(self, *args, **kwargs):
        response = requests.get('http://www.mondotravel.hr/ljetno-putovanje-zrakoplovom-amsterdam-i-nizozemska.html')
