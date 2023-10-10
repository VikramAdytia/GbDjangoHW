from django.urls import path 
from . import views
from .views import client_orders_n_days, client_form, product_form

urlpatterns = [
    path('', views.index, name='main'),
    path('about/', views.about, name='about'),
    path('client/<int:client_id>/<int:n>/', client_orders_n_days, name='client_orders_n_days'),
    path('client/add/', client_form, name='client_form'),
    path('product/add/', product_form, name='product_form'),
]