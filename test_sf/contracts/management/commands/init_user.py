from django.core.management.base import BaseCommand
from dotenv import load_dotenv
from django.contrib.auth.models import User
import logging
import os

_logger = logging.getLogger(__name__)

load_dotenv()


class Command(BaseCommand):
    help = 'Help to create supperuser'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if not User.objects.filter(username=username).exists():
            _logger.info('Creating account for %s (%s)' % (username, email))
            User.objects.create_superuser(
                email=email, username=username, password=password)
        else:
            _logger.info('Admin account has already been initialized.')
