from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    context = {
        'title' : 'Helloooo',
        'content' : 'Welcome to the homepage.'
    }
    return render(request, 'home_page.html', context)

def about_page(request):
    context = {
        'title' : 'About Page',
        'content' : 'Welcome to the about page.'
    }
    return render(request, 'home_page.html', context)

def contact_page(request):
    context = {
        'title' : 'Contact Page',
        'content' : 'Welcome to the contact page.'
    }
    return render(request, 'home_page.html', context)