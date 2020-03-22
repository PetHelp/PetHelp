from uuid import uuid4

from django.db import IntegrityError
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, filters
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from pet_help.filters import HelpOfferFilterSet, HelpRequestFilterSet, MessageFilterSet
from pet_help.models import Animal, User, HelpRequest, HelpOffer, Message, AnimalType, HelpType
from pet_help.permissions import OwnerReadWritePermission, PublicReadOwnerWritePermission
from pet_help.serializers import UserSerializer, AnimalSerializer, HelpRequestSerializer, \
    HelpOfferSerializer, MessageSerializer


class UserViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class AnimalViewSet(ModelViewSet):
    serializer_class = AnimalSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    permission_classes = (OwnerReadWritePermission,)
    queryset = Animal.objects.all()
    ordering_fields = ['name', 'active']

    def get_queryset(self):
        return Animal.objects.filter(owner=self.request.user)


class HelpRequestViewSet(ModelViewSet):
    serializer_class = HelpRequestSerializer
    queryset = HelpRequest.objects.all()
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    permission_classes = (PublicReadOwnerWritePermission,)
    filterset_class = HelpRequestFilterSet
    ordering_fields = ['created_at', 'type']


class HelpOfferViewSet(ModelViewSet):
    serializer_class = HelpOfferSerializer
    queryset = HelpOffer.objects.all()
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    permission_classes = (PublicReadOwnerWritePermission,)
    filterset_class = HelpOfferFilterSet
    ordering_fields = ['created_at', 'type']


class MessageViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    serializer_class = MessageSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    permission_classes = (IsAuthenticated,)
    queryset = Message.objects.all()
    filterset_class = MessageFilterSet
    ordering_fields = ['created_at']

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(Q(sender=user) | Q(receiver=user))


@api_view(http_method_names=["GET"])
def list_animal_types(request):
    animal_types = [animal_type.value for animal_type in AnimalType]
    return JsonResponse(animal_types, status=200, safe=False)


@api_view(http_method_names=["GET"])
def list_help_types(request):
    help_types = [help_type.value for help_type in HelpType]
    return JsonResponse(help_types, status=200, safe=False)


@api_view(http_method_names=["POST"])
def register(request):
    email = request.data.get("email")
    password = request.data.get("password")
    if email and password:
        try:
            User.objects.create_user(email, email, password)
            return HttpResponse(status=201)
        except IntegrityError as ie:
            return JsonResponse(dict(email="This email address is already taken"), status=400)
        except Exception as e:
            raise e
    return JsonResponse(dict(info="All fields must be set"), status=400)


@api_view(http_method_names=["POST"])
def reset_password(request):
    email = request.data.get("email")
    user = User.objects.filter(email=email).first()
    if email and user:
        new_password = uuid4()
        user.set_password(new_password)
        user.save()

        if request.data.get("send_to_emergency_contact"):
            pass
            # TODO: send email with new pw to user.emergency_contact_email
        else:
            pass
            # TODO: send email with new pw to user.email
        return HttpResponse(status=200)
    return JsonResponse(dict(email="User not found"), status=400)
