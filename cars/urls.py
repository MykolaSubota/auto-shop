from django.urls import path
from cars.views import AutoHomeListView

app_name = 'cars'

urlpatterns = [
    path('',
         AutoHomeListView.as_view(),
         name='home'),
]
