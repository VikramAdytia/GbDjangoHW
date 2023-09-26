from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),  # по пустой строке у нас вызывется фу-ция index
    path('about/', views.about, name='about'),  # по строке about после адреса сервера вызывается функция about
]
