from django.core.management.base import BaseCommand
from dz_ORMapp.models import Client

class Command(BaseCommand):
    help="Update client telephone by id." 
    
    def add_arguments(self,parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('telephone', type=int, help='Client telephone')
        
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        tel = kwargs.get('telephone')
        client = Client.objects.filter(pk=pk).first() 
        client.tel = tel 
        client.save() 
        self.stdout.write(f'{client}')
