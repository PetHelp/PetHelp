from django.contrib.auth.models import AbstractUser
from django.db import models
from enumfields import Enum, EnumField


class AnimalType(Enum):
    DOG = "DOG"


class AnimalTag(Enum):
    DOG = "DOG"


class HelpType(Enum):
    DOG = "DOG"


class Role(models.Model):
    name = models.CharField(max_length=100)


class User(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    role = models.ForeignKey(Role, related_name="users", on_delete=models.PROTECT, null=True,
                             blank=True)
    bio = models.CharField(max_length=1024, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    emergency_contact_email = models.CharField(max_length=150, blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    registered_at = models.DateField(auto_now_add=True)
    last_login = models.DateField(null=True, blank=True)
    virtual = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Animal(models.Model):
    name = models.CharField(max_length=50)
    type = EnumField(AnimalType, max_length=50)
    image = models.TextField(blank=True, null=True) # FIXME: use FileField in production state
    owner = models.ForeignKey(User, related_name="animals", on_delete=models.CASCADE)
    care_person = models.ForeignKey(User, null=True, blank=True, related_name="cared_animals",
                                    on_delete=models.SET_NULL)
    current_address = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)


class HelpRequest(models.Model):
    user = models.ForeignKey(User, related_name="help_requests", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    type = EnumField(HelpType, max_length=20)
    description = models.CharField(max_length=1024)
    active = models.BooleanField(default=True)
    animals = models.ManyToManyField(Animal, related_name="animals")


class HelpOffer(models.Model):
    user = models.ForeignKey(User, related_name="help_offers", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    type = EnumField(HelpType, max_length=20)
    description = models.CharField(max_length=1024)
    active = models.BooleanField(default=True)


class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.SET_NULL,
                               null=True, blank=True)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.SET_NULL,
                                 null=True, blank=True)
    related_help_offer = models.ForeignKey(HelpOffer, null=True, blank=True,
                                           related_name="offer_messages",
                                           on_delete=models.SET_NULL)
    related_help_request = models.ForeignKey(HelpRequest, null=True, blank=True,
                                             related_name="request_messages",
                                             on_delete=models.SET_NULL)
    text = models.CharField(max_length=1024)
