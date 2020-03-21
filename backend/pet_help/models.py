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


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    role = models.ForeignKey(Role, related_name="users", on_delete=models.CASCADE)
    bio = models.CharField(max_length=1024)
    address = models.CharField(max_length=50)
    emergency_contact_email = models.CharField(max_length=150)
    image = models.TextField()
    registered_at = models.DateField()
    last_login = models.DateField()
    virtual = models.BooleanField(default=False)


class Animal(models.Model):
    name = models.CharField(max_length=50)
    type = EnumField(AnimalType, max_length=50)
    image = models.TextField()
    owner = models.ForeignKey(User, related_name="animals", on_delete=models.CASCADE)
    care_person = models.ForeignKey(User, null=True, blank=True, related_name="cared_animals",
                                    on_delete=models.SET_NULL)
    current_address = models.CharField(max_length=150)
    description = models.CharField(max_length=1024)


class HelpRequest(models.Model):
    user = models.ForeignKey(User, related_name="help_requests", on_delete=models.CASCADE)
    created_at = models.DateField()
    type = EnumField(HelpType, max_length=20)
    description = models.CharField(max_length=1024)
    active = models.BooleanField(default=True)


class HelpOffer(models.Model):
    user = models.ForeignKey(User, related_name="help_offers", on_delete=models.CASCADE)
    created_at = models.DateField()
    type = EnumField(HelpType, max_length=20)
    description = models.CharField(max_length=1024)
    active = models.BooleanField(default=True)


class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.SET_NULL,
                               null=True, blank=True)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.SET_NULL, null=True, blank=True)
    related_help_offer = models.ForeignKey(HelpOffer, null=True, blank=True,
                                           related_name="offer_messages", on_delete=models.SET_NULL)
    related_help_request = models.ForeignKey(HelpRequest, null=True, blank=True,
                                             related_name="request_messages", on_delete=models.SET_NULL)
    text = models.CharField(max_length=1024)
