from django.views.generic import ListView, DetailView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

# Если есть contacts — добавь
from django.views.generic.base import TemplateView

class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'