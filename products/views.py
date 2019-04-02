from __future__ import unicode_literals

from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect

from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context