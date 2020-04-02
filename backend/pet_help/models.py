from django.contrib.auth.models import AbstractUser
from django.db import models
from enumfields import Enum, EnumField


class AnimalType(Enum):
    DOG = "DOG"
    CAT = "CAT"
    TERRARIUM = "TERRARIUM"
    AQUARIUM = "AQUARIUM"
    HORSE = "HORSE"
    BIRD = "BIRD"
    NAGETIER = "NAGETIER"
    OTHER = "OTHER"


class AnimalTag(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    CASTRATED = "CASTRATED"
    VERTRÄGLICH_MIT_KATZEN = "VERTRÄGLICH_MIT_KATZEN"
    VERTRÄGLICH_MIT_HUNDEN = "VERTRÄGLICH_MIT_HUNDEN"
    VERTRÄGLICH_MIT_KINDERN = "VERTRÄGLICH_MIT_KINDERN"


class DogTag(Enum):
    GROSS = "GROSS"  ## >= 30 kg
    MITTEL = "MITTEL"  ## 10 kg >= hund > 30 kg
    KLEIN = "KLEIN"  ## hund < 10 kg
    MUZZLE = "MUZZLE"
    SACHKUNDENACHWEIS2040 = "2040SACHKUNDENACHWEIS"
    SACHKUNDENACHWEISLISTE = "LISTENHUNDSACHKUNDENACHWEIS"


class CatTag(Enum):
    FREIGÄNGER = "FREIGÄNGER"


class TerrariumTag(Enum):
    GIFTIG = "GIFTIG"
    GRUPPENHALTUNG = "GRUPPENHALTUNG"


class AqariumTag(Enum):
    GRUPPENHALTUNG = "GRUPPENHALTUNG"
    SALZWASSER = "SALZWASSER"
    SÜSSWASSER = "SÜSSWASSER"


class HorseTag(Enum):
    PONY = "PONY"
    PFERD = "PFERD"


class HelpType(Enum):
    GASSI_GEHEN = "GASSI_GEHEN"
    FUTTER_KAUFEN = "FUTTER_KAUFEN"
    HEIMBETREUUNG = "HEIMBETREUUNG"


class Role(models.Model):
    name = models.CharField(max_length=100)


class User(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    role = models.ForeignKey(
        Role, related_name="users", on_delete=models.PROTECT, null=True, blank=True
    )
    bio = models.CharField(max_length=1024, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    address_lat = models.CharField(max_length=20, blank=True, null=True)
    address_lng = models.CharField(max_length=20, blank=True, null=True)
    emergency_contact_email = models.CharField(max_length=150, blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    registered_at = models.DateField(auto_now_add=True)
    last_login = models.DateField(null=True, blank=True)
    virtual = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=True)
    # FIXME: change default of email_verified to False and implement email verification

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Animal(models.Model):
    name = models.CharField(max_length=50)
    type = EnumField(AnimalType, max_length=50)
    image = models.TextField(blank=True, null=True)  # FIXME: use FileField in production state
    owner = models.ForeignKey(User, related_name="animals", on_delete=models.CASCADE)
    care_person = models.ForeignKey(
        User, null=True, blank=True, related_name="cared_animals", on_delete=models.SET_NULL
    )
    description = models.CharField(max_length=1024, blank=True, null=True)


class HelpRequest(models.Model):
    user = models.ForeignKey(User, related_name="help_requests", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    type = EnumField(HelpType, max_length=20)
    description = models.CharField(max_length=1024)
    active = models.BooleanField(default=True)
    animals = models.ManyToManyField(Animal, related_name="requests")
    address = models.CharField(max_length=50, blank=True, null=True)
    address_lat = models.CharField(max_length=20, blank=True, null=True)
    address_lng = models.CharField(max_length=20, blank=True, null=True)


class HelpOffer(models.Model):
    user = models.ForeignKey(User, related_name="help_offers", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    type = EnumField(HelpType, max_length=20)
    description = models.CharField(max_length=1024)
    active = models.BooleanField(default=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    address_lat = models.CharField(max_length=20, blank=True, null=True)
    address_lng = models.CharField(max_length=20, blank=True, null=True)


class Message(models.Model):
    sender = models.ForeignKey(
        User, related_name="sent_messages", on_delete=models.SET_NULL, null=True, blank=True
    )
    receiver = models.ForeignKey(
        User, related_name="received_messages", on_delete=models.SET_NULL, null=True, blank=True
    )
    related_help_offer = models.ForeignKey(
        HelpOffer, null=True, blank=True, related_name="offer_messages", on_delete=models.SET_NULL
    )
    related_help_request = models.ForeignKey(
        HelpRequest,
        null=True,
        blank=True,
        related_name="request_messages",
        on_delete=models.SET_NULL,
    )
    text = models.CharField(max_length=1024)
