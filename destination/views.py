from django.views.generic import DetailView
from destination.models import Destination, Review


class DestinationDetailView(DetailView):
    queryset = Destination.objects.all()
    template_name = 'destination.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        destination = context['object']
        context['reviews'] = Review.objects.filter(
            destination=destination
        ).order_by('-date_posted')
        return context
