from django.urls import path
from django.views.generic import TemplateView

from cars.views import AutoHomeListView, AutoListView, AutoDetailView

app_name = 'cars'

urlpatterns = [
    path('',
         AutoHomeListView.as_view(),
         name='home'),
    path('list/',
         AutoListView.as_view(),
         name='car_list'),
    # path('car/',
    #      TemplateView.as_view(template_name='cars/car.html'),
    #      name='car_detail')
    path('car/<int:pk>/',
         AutoDetailView.as_view(),
         name='car_detail'),
]
