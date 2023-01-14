from django.urls import path, include
from . import views

app_name = 'nangman'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
]
