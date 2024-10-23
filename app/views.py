from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from app.models import Product


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class ShopListView(ListView):
    template_name = 'shop.html'
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class ShopDetailView(TemplateView):
    template_name = 'shop-detail.html'


class CreateShopView(CreateView):
    template_name = 'create.html'
    model = Product
    fields = "__all__"
    success_url = reverse_lazy('shop-list')