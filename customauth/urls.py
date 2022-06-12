from django.urls import path
from .views import RequestCreateView

app_name = 'customauth'

urlpatterns = [
    path('',
         RequestCreateView.as_view(),
         name='contact'),
]
