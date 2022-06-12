from django.shortcuts import render
from django.views.generic import ListView, DetailView

from cars.models import Auto


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
