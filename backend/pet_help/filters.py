from django_filters import rest_framework as filters

from pet_help.models import HelpOffer, HelpRequest, Message


class HelpOfferFilterSet(filters.FilterSet):

    class Meta:
        model = HelpOffer
        fields = ['type', 'active']


class HelpRequestFilterSet(filters.FilterSet):
    distance = filters.NumberFilter(method='filter_by_distance')

    def filter_by_distance(self, queryset, name, value):
        return queryset

    class Meta:
        model = HelpRequest
        fields = ['type', 'active']


class MessageFilterSet(filters.FilterSet):
    class Meta:
        model = Message
        fields = ['receiver', 'sender', 'related_help_offer', 'related_help_request']
