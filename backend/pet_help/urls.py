from django.conf.urls import include
from django.urls import re_path
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt import views as jwt_views

from pet_help.views import UserViewSet, AnimalViewSet, HelpRequestViewSet, HelpOfferViewSet, \
    MessageViewSet, register, reset_password, list_animal_types, list_help_types, handler404view, \
    verify_email

router = routers.DefaultRouter()

router.register("users", UserViewSet)
router.register("animals", AnimalViewSet)
router.register("help-requests", HelpRequestViewSet)
router.register("help-offers", HelpOfferViewSet)
router.register("messages", MessageViewSet)

urlpatterns = [
    re_path("api/", include(router.urls)),
    re_path("api/animal-types", list_animal_types, name="animal-types"),
    re_path("api/help-types", list_help_types, name="help-types"),
    re_path('api/register/', register, name='register'),
    re_path('api/reset-password/', reset_password, name='register'),
    re_path('api/verify-email/', verify_email, name='register'),
    re_path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    re_path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),

    re_path('api/docs/openapi/', get_schema_view(
        title="Quarantiere.de Api Docs", description="", version="1.0.0", public=True
    ), name='openapi-schema'),
    re_path('api/docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),

    #url(r"api/ht/", include("health_check.urls"))
]

handler404 = handler404view
