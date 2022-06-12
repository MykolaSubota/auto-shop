from django.urls import path
from django.views.generic import TemplateView

from cars.views import AutoHomeListView, AutoListView

app_name = 'cars'

urlpatterns = [
    path('',
         AutoHomeListView.as_view(),
         name='home'),
    path('list/',
         AutoListView.as_view(),
         name='car_list'),
]
