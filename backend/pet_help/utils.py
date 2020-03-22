from django.http import JsonResponse
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
        response = JsonResponse(data=dict(info="error"), status=response.status_code)

    return response
