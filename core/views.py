from django.http import HttpResponse
from django.views.generic import View, ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from django_filters.views import FilterView

from core.models import Product
from core import filters


class FirstView(View):
    def get(self, request):
        return HttpResponse(' Hi Django!')


class ProductsList(FilterView):
    model = Product
    template_name = 'produce_shelf/produce_shelf.html'
    context_object_name = 'produces'
    filterset_class = filters.Product


class ProductDetail(DetailView):
    model = Product
    template_name = 'produce_shelf/produce_detail.html'
    context_object_name = 'produce'


class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'price', 'status', 'image']
    template_name = 'produce_shelf/produce_form.html'

    def get_success_url(self):
        return reverse_lazy('produce_detail', kwargs={'pk': self.object.pk})


class ProductUpdate(UpdateView):
    model = Product
    template_name = 'produce_shelf/produce_update.html'
    fields = ['name', 'price']

    def get_success_url(self):
        return reverse_lazy('produce_shelf')


class ProductDelete(DeleteView):
    model = Product
    template_name = 'produce_shelf/produce_confirm_delete.html'
    success_url = reverse_lazy('produce_shelf')
