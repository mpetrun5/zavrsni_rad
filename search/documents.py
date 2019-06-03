from django_elasticsearch_dsl import DocType, Index
from django_elasticsearch_dsl import fields

from destination.models import Destination

destination = Index('destinations')
destination.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@destination.doc_type
class DestinationDocument(DocType):
    price = fields.FloatField(attr=None)
    agency = fields.TextField(attr='agency_to_string')
    original_link = fields.TextField(attr='original_url_to_string')

    class Meta:
        model = Destination

        fields = [
            'id',
            'image',
            'name',
            'description',
            'num_of_nights',
        ]
