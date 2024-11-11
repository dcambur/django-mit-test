from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_welcome_email(user_id):
    from django.contrib.auth.models import User
    user = User.objects.get(id=user_id)

    subject = 'Welcome to our site!'
    message = f'Welcome {user.username}! You have successfully created account on our site!'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list)
