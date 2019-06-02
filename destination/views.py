from django.views.generic import DetailView
from destination.models import Destination


class DestinationDetailView(DetailView):
    queryset = Destination.objects.all()
    template_name = 'destination.html'
