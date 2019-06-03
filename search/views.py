
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
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

        page = self.request.GET.get('page', 1)
        q = self.request.GET.get('q')

        price = self.request.GET.get('price')
        if price:
            price_min, price_max = price.split(',')
        else:
            price_min = 0
            price_max = 60000

        num_of_nights = self.request.GET.get('num_of_nights')
        if num_of_nights:
            num_of_nights_min, num_of_nights_max = num_of_nights.split(',')
        else:
            num_of_nights_min = 0
            num_of_nights_max = 30

        form_data = {
            'q': q
        }
        if q:
            query = MultiMatch(query=q, fields=['name', 'description'], fuzziness='AUTO')
            destinations = list(
                DestinationDocument.search().query(
                    query
                )[0:1000]
            )
            if price:
                destinations = [
                    destination for destination in destinations
                    if destination.num_of_nights <= int(num_of_nights_max)
                    and destination.num_of_nights >= int(num_of_nights_min)
                ]
            if num_of_nights:
                destinations = [
                    destination for destination in destinations
                    if destination.price <= int(price_max)
                    and destination.price >= int(price_min)
                ]

            paginator = Paginator(destinations, 8)
            try:
                destinations = paginator.page(page)
            except PageNotAnInteger:
                destinations = paginator.page(1)
            except EmptyPage:
                destinations = paginator.page(paginator.num_pages)

        context['search_form'] = SearchForm(data=form_data)
        context['destinations'] = destinations

        return context
