from rest_framework import serializers

from pet_help.models import Animal, User, Message, HelpRequest, HelpOffer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ()


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        exclude = ()


class HelpRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpRequest
        exclude = ()


class HelpOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpOffer
        exclude = ()


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ()

