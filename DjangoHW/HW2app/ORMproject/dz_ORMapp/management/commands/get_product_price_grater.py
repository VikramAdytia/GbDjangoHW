from django.core.management.base import BaseCommand
from dz_ORMapp.models import Product

class Command(BaseCommand):
    help="Get products grater than <price>." 
    
    def add_arguments(self,parser): 
        parser.add_argument('price', type=float, help='Product price') 
        
    def handle(self, *args, **kwargs):
        price = kwargs['price']
        procuct=Product.objects.filter(price__gt=price)
        self.stdout.write(f'{procuct}')
        