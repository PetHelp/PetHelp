from datetime import datetime

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver


@receiver(user_logged_in)
def post_login(sender, user, request, **kwargs):
    # FIXME: this is currently not working because signal is not sent on token auth
    user.last_login = datetime.now()
    user.save()

