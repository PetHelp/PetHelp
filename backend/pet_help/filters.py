from django_filters import rest_framework as filters
from django.db.models import Func, F

from pet_help.models import HelpOffer, HelpRequest, Message
from pet_help.services import geo_service


class HelpOfferFilterSet(filters.FilterSet):
    class Meta:
        model = HelpOffer
        fields = ["type", "active"]


class HelpRequestFilterSet(filters.FilterSet):
    max_distance = filters.NumberFilter(method="filter_by_distance")

    def filter_by_distance(self, queryset, name, value):
        """
        request_location = self.request.query_params.get('location')
        if request_location and value:
            request_location_geo = geo_service.get_geo_coordinates_for_address('{} Germany'.format(request_location))
            # FIXME: this will be slow and resource hungry and must be optimized
            filter_ids = []
            for request in queryset.select_related('animals'):
                distance = geo_service.get_distance_between_points_in_km(
                    request_location_geo['lat'], request_location_geo['lng'],
                    request.animal.current_address_lat, request.animal.current_address_lng)
                if distance <= value:
                    filter_ids.append(request.id)
            return queryset.filter(id__in=filter_ids)
        """
        return queryset

    class Meta:
        model = HelpRequest
        fields = ["type", "active"]


class MessageFilterSet(filters.FilterSet):
    class Meta:
        model = Message
        fields = ["receiver", "sender", "related_help_offer", "related_help_request"]
