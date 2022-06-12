from django.forms import ModelForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from cars.models import Auto
from customauth.models import Order


def base_template(request):
    return render(request, 'base.html')


class AutosListMixin(ListView):
    model = Auto


class AutoHomeListView(AutosListMixin):
    template_name = 'cars/home.html'


class AutoListView(AutosListMixin):
    template_name = 'cars/cars.html'
    paginate_by = 12


class AutoDetailView(DetailView):
    template_name = 'cars/car.html'
    model = Auto


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('last_name', 'first_name', 'email', 'phone', 'auto', 'complete_set', 'note')


class OrderCreateView(CreateView):
    template_name = 'cars/car.html'
    # model = Order
    success_url = reverse_lazy('cars:home')
    form_class = OrderForm
