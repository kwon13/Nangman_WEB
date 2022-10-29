from django.urls import path, include
from . import views

app_name = 'nangman'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/<str:desc>', views.search, name='search'),
    path('debug_search/<str:desc>', views.debug_search, name='debug_search'),
]
