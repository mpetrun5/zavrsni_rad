import json

from django.views import View
from elasticsearch_dsl.query import MultiMatch

from search.documents import DestinationDocument


class SearchView(View):

    def get(self, request):
        q = request.GET.get('q')

        if q:
            query = MultiMatch(query=q, fields=['name'], fuzziness='AUTO')
            destinations = DestinationDocument.search().query(
                query
            )
        for destination in destinations:
            print(destination.name)

        return json.dumps({})
