import datetime
import random

from django.core.management.base import BaseCommand
from dz_1.models import User, Product,Order

class Command(BaseCommand):
    help = "Creates postts to fill db"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of products to create per user')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        users = User.objects.all()
        product_all = Product.objects.all()
        for user in users:
            for j in range(5):
                order = Order(customer=user, total_price=10)
                order.save()
                self.stdout.write(self.style.SUCCESS(f'Created {order}'))
                for i in range(2):
                    product = random.choice(product_all)
                    # print(f'user= {user},product={product}')
                    order.products.add(product)


