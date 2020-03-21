from drf_enum_field.serializers import EnumFieldSerializerMixin
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from pet_help.models import Animal, User, Message, HelpRequest, HelpOffer


class UserSerializer(EnumFieldSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ()

    def create(self, validated_data):
        raise NotImplementedError()


class AnimalSerializer(EnumFieldSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Animal
        exclude = ()
        read_only_fields = ('id', 'owner')

    def validate(self, attrs):
        attrs.pop("owner", None)
        return attrs

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)


class HelpRequestSerializer(EnumFieldSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = HelpRequest
        exclude = ()
        read_only_fields = ('id', 'user')

    def validate(self, attrs):
        attrs.pop("owner", None)
        return attrs

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class HelpOfferSerializer(EnumFieldSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = HelpOffer
        exclude = ()
        read_only_fields = ('id', 'user')

    def validate(self, attrs):
        attrs.pop("owner", None)
        return attrs

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ()

    def validate(self, attrs):
        related_field = attrs.get("related_help_offer") or attrs.get("related_help_request")
        if not related_field:
            raise ValidationError(detail="related_help_offer or related_help_request must be set")

        if attrs["receiver"] != related_field.user:
            raise ValidationError(detail="Given receiver does not match related fields owner")
        return attrs

    def create(self, validated_data):
        validated_data["sender"] = self.context["request"].user
        return super().create(validated_data)


