from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Request


class RequestCreateView(CreateView):
    model = Request
    template_name = 'contact.html'
    fields = ('name', 'email', 'subject', 'message')
    success_url = reverse_lazy('cars:home')
