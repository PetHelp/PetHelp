from django.conf.urls import include, url
from django.urls import re_path
from rest_framework import routers

router = routers.DefaultRouter()

#router.register("pets", PetsViewSet)

urlpatterns = [re_path("", include(router.urls)), url(r"^ht/", include("health_check.urls"))]
