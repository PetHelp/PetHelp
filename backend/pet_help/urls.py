from django.conf.urls import include, url
from django.urls import re_path
from rest_framework import routers

from pet_help.views import UserViewSet, AnimalViewSet, HelpRequestViewSet, HelpOfferViewSet, \
    MessageViewSet

router = routers.DefaultRouter()

router.register("users", UserViewSet)
router.register("animals", AnimalViewSet)
router.register("help-requests", HelpRequestViewSet)
router.register("help-offers", HelpOfferViewSet)
router.register("messages", MessageViewSet)

urlpatterns = [
    re_path("", include(router.urls)),
    url(r"^ht/", include("health_check.urls"))
]
