from django.conf.urls import include, url
from django.urls import re_path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from pet_help.views import UserViewSet, AnimalViewSet, HelpRequestViewSet, HelpOfferViewSet, \
    MessageViewSet, register, reset_password

router = routers.DefaultRouter()

router.register("users", UserViewSet)
router.register("animals", AnimalViewSet)
router.register("help-requests", HelpRequestViewSet)
router.register("help-offers", HelpOfferViewSet)
router.register("messages", MessageViewSet)

urlpatterns = [
    re_path("", include(router.urls)),
    re_path('register/', register, name='register'),
    re_path('reset-password/', reset_password, name='register'),
    re_path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    url(r"^ht/", include("health_check.urls"))
]
