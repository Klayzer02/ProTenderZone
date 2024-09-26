from django.urls import path
from .views import *

app_name = 'devices'

urlpatterns = [
    path('', index, name='index'),
    path('GOS/', devices_page, name='devices_page'),
    path('Samruk/', devices_page, name='devices_page2'),
]
