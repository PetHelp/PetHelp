from drf_enum_field.serializers import EnumFieldSerializerMixin
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from pet_help import services
from pet_help.models import Animal, User, Message, HelpRequest, HelpOffer


class UserSerializer(EnumFieldSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('id', 'password', 'role', 'virtual', 'first_name', 'last_name', 'is_staff',
                   'groups', 'user_permissions', 'is_superuser', 'date_joined', 'is_active',
                   'username')
        read_only_fields = ('address_lat', 'address_lng')

    def validate(self, attrs):
        attrs.pop("password", None)
        return attrs

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        if "address" in validated_data and validated_data.get("address") != instance.address:
            updated_instance = super().update(instance, validated_data)
            updated_instance = services.resolve_geo_for_user(updated_instance)
            return updated_instance
        else:
            return super().update(instance, validated_data)


class ReducedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'image', 'bio')

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class AnimalSerializer(EnumFieldSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Animal
        exclude = ()
        read_only_fields = ('id', 'owner', 'current_address_lat', 'current_address_lng')

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        instance = super().create(validated_data)
        instance = services.resolve_geo_for_animal(instance)
        return instance

    def update(self, instance, validated_data):
        if "current_address" in validated_data and \
                validated_data.get("current_address") != instance.current_address:
            updated_instance = super().update(instance, validated_data)
            updated_instance = services.resolve_geo_for_animal(updated_instance)
            return updated_instance
        else:
            return super().update(instance, validated_data)


class ReducedAnimalSerializer(EnumFieldSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Animal
        exclude = ('id', 'owner', 'care_person', 'current_address', 'current_address_lat',
                   'current_address_lng')

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class HelpRequestSerializer(EnumFieldSerializerMixin, serializers.ModelSerializer):
    animals = ReducedAnimalSerializer(many=True)
    user = ReducedUserSerializer(read_only=True)

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
    user = ReducedUserSerializer(read_only=True)

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


