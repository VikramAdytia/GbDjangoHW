# from django.shortcuts import render
import logging
from datetime import timedelta, date

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django import forms

from .models import Client, Order, Product
from .forms import ClientForm, ProductForm

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

def client_orders_n_days(request, client_id, n):
    startdate = date.today()
    enddate = startdate + timedelta(days=n)
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client=client).filter(date__range=[startdate, enddate]).order_by('date_ordered') # ???
    return render(request, 'dz_ORMapp/client_orders.html', {'client': client, 'orders':orders})

def client_form(request):
    if request.method =='POST':
        form = ClientForm(request.POST)
        message='Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            tel = form.cleaned_data['tel']
            address = form.cleaned_data['address']
            logger.info(f'Client: {name=}, {email=}, {tel=}, {address=}')
            client = Client(name=name, email=email, tel=tel, address=address)
            client.save()
            message='Пользователь сохранён'
    else:
        form = ClientForm()
        message = 'Заполните форму'
    return render(request, 'dz_ORMapp/client_form.html', {'form': form, 'message': message})

def product_form(request):
    if request.method =='POST':
        form = ProductForm(request.POST, request.FILES)
        message='Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            foto = form.cleaned_data['foto']
            quantity = form.cleaned_data['quantity']
            product = Product(name=name, description=description, price=price, foto=foto, quantity=quantity)
            fs = FileSystemStorage()
            fs.save(foto.name, foto)
            product.save()
            logger.info(f'Got: {form.cleaned_data=}')
            message='Продукт сохранён'
    else:
        form = ProductForm()
        message = 'Заполните форму'
    return render(request, 'dz_ORMapp/product_form.html', {'form': form, 'message': message})
