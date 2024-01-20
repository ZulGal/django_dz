import datetime
import decimal
import random

from django.core.management.base import BaseCommand
from dz_1.models import Product

class Command(BaseCommand):
    help = "Create new product."

    def handle(self, *args, **kwargs):
        for i in range (1,11):
            product = Product(
                title=f'Title {i}',
                description=f'Lorem ipsum',
                price = 10,
                quantity = random.randint(1, 6),
                # price= decimal.Decimal(random.randrange(10000))/100,
                # quantity = random.randint(1, 10),
            )
            self.stdout.write(self.style.ERROR(f'Product{product} created'))
            product.save()