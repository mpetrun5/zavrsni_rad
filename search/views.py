import json

from django.views import View

from search.documents import DestinationDocument


class SearchView(View):

    def get(self, request):
        q = request.GET.get('q')

        if q:
            destinations = DestinationDocument.search().suggest(
                'destinations',
                q,
                term={
                    'field': 'name',
                }
            )

        return json.dumps(destinations)
