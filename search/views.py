from django.views.generic import TemplateView
from elasticsearch_dsl.query import MultiMatch

from search.documents import DestinationDocument
from search.forms import SearchForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm()
        return context


class SearchView(TemplateView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        q = self.request.GET.get('q')
        if q:
            query = MultiMatch(query=q, fields=['name'], fuzziness='AUTO')
            context['destinations'] = DestinationDocument.search().query(
                query
            )
        context['search_form'] = SearchForm()
        return context
