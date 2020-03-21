from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from pet_help.models import Animal, User, HelpRequest, HelpOffer, Message
from pet_help.serializers import UserSerializer, AnimalSerializer, HelpRequestSerializer, \
    HelpOfferSerializer, MessageSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = (DjangoFilterBackend,)


class AnimalViewSet(ModelViewSet):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()
    filter_backends = (DjangoFilterBackend,)


class HelpRequestViewSet(ModelViewSet):
    serializer_class = HelpRequestSerializer
    queryset = HelpRequest.objects.all()
    filter_backends = (DjangoFilterBackend,)


class HelpOfferViewSet(ModelViewSet):
    serializer_class = HelpOfferSerializer
    queryset = HelpOffer.objects.all()
    filter_backends = (DjangoFilterBackend,)


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    filter_backends = (DjangoFilterBackend,)
