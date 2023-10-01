# from django.shortcuts import render
import logging
from datetime import timedelta, date

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Client, Order

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Main page accessed')
    html = """
        My name is Vikram."""
    return HttpResponse(f'<h1>{html}</h1>') 

def about(request):
    html = """
        This is my first <b>Django-site</b>.<br>
        <i>And I hope, not the last one.</i> :)
        """
    logger.debug('About page accessed')
    return HttpResponse(html) 

def client_orders_7days(request, client_id):
    startdate = date.today()
    enddate = startdate + timedelta(days=6)
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client=client).filter(date__range=[startdate, enddate]).order_by('date_ordered') # ???
    return render(request, 'myapp3/client_orders.html', {'client': client,'orders':orders})
