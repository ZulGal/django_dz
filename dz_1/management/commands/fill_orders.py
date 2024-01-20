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
            for i in range(count):
                product = random.choice(product_all)
                print(f'user= {user},product={product}, total_price={product.price}')

                order = Order(
                    customer = user,
                    # Direct assignment to the forward side of a many-to-many set is prohibited
                    products = product,
                    total_price = product.price,
                )
                self.stdout.write(self.style.SUCCESS(f'Created {order}'))
                order.save()