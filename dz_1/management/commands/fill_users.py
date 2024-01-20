import datetime

from django.core.management.base import BaseCommand
from dz_1.models import User

class Command(BaseCommand):
    help = "Create new user."

    def handle(self, *args, **kwargs):
        for i in range (1,11):
            user = User(
                name=f'User {i}',
                email=f'mail{i}@example.com',
                phone= '+7(901)-999-99-99',
                address = '100100,City{i}',

            )
            self.stdout.write(self.style.ERROR(f'User{user} created'))
            user.save()