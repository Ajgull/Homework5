from django.http import HttpResponse
from django.views.generic import View, TemplateView

from core.models import Product


class FirstView(View):
    def get(self, request):
        return HttpResponse(' Hi Django!')


class ListView(TemplateView):
    template_name = 'produce_shelf/produce_shelf.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produce'] = Product.objects.all()
        return context
