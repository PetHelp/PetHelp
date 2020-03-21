from django.db import IntegrityError
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from pet_help.models import Animal, User, HelpRequest, HelpOffer, Message
from pet_help.permissions import OwnerReadWritePermission, PublicReadOwnerWritePermission
from pet_help.serializers import UserSerializer, AnimalSerializer, HelpRequestSerializer, \
    HelpOfferSerializer, MessageSerializer


@api_view(http_method_names=["POST"])
def register(request):
    name = request.data.get("name")
    email = request.data.get("email")
    password = request.data.get("password")

    if email and password and name:
        try:
            User.objects.create_user(name, email, password)
            return HttpResponse(status=201)
        except IntegrityError:
            return JsonResponse(dict(email="This email address is already taken"), status=400)
        except Exception as e:
            raise e
    return JsonResponse(dict(info="All fields must be set"), status=400)


class UserViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class AnimalViewSet(ModelViewSet):
    serializer_class = AnimalSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (OwnerReadWritePermission,)
    queryset = Animal.objects.all()

    def get_queryset(self):
        return Animal.objects.filter(owner=self.request.user)


class HelpRequestViewSet(ModelViewSet):
    serializer_class = HelpRequestSerializer
    queryset = HelpRequest.objects.all()
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (PublicReadOwnerWritePermission,)


class HelpOfferViewSet(ModelViewSet):
    serializer_class = HelpOfferSerializer
    queryset = HelpOffer.objects.all()
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (PublicReadOwnerWritePermission,)


class MessageViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    serializer_class = MessageSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (IsAuthenticated,)
    queryset = Message.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(Q(sender=user) | Q(receiver=user))
