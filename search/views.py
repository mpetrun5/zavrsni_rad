
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import TemplateView
from elasticsearch_dsl.query import MultiMatch

from destination.models import Destination, Review
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

    def paginate(self, destinations, page):
        paginator = Paginator(destinations, 8)
        try:
            destinations = paginator.page(page)
        except PageNotAnInteger:
            destinations = paginator.page(1)
        except EmptyPage:
            destinations = paginator.page(paginator.num_pages)

        return destinations

    def calculate_reviews(self, destinations):
        """
        Add num of reviews and range of stars to destinations.
        """
        for destination in destinations:
            destination_model = Destination.objects.get(pk=destination.id)
            avg_rating, destination.num_of_reviews = Review.calculate_average_rating(
                destination_model
            )
            destination.gray_stars = range(5 - int(avg_rating))
            destination.yellow_stars = range(int(avg_rating))

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

        query = MultiMatch(query=q, fields=['name', 'description'], fuzziness='AUTO')
        destinations = list(
            DestinationDocument.search().query(
                query
            )[0:1000]
        )

        # Understand this a bad idea, but kinda in a hurry
        if price or num_of_nights:
            destinations = [
                destination for destination in destinations
                if
                (
                    destination.num_of_nights <= int(num_of_nights_max)
                    and destination.num_of_nights >= int(num_of_nights_min)
                )
                or
                (
                    destination.price <= int(price_max)
                    and destination.price >= int(price_min)
                )
            ]

        self.calculate_reviews(destinations)
        destinations = self.paginate(destinations, page)

        context['search_form'] = SearchForm(data={'q': q})
        context['destinations'] = destinations
        context['price_min'] = price_min
        context['price_max'] = price_max
        context['num_of_nights_min'] = num_of_nights_min
        context['num_of_nights_max'] = num_of_nights_max

        return context
