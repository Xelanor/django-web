# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
import os
from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.urls import reverse

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(123165, 5416513218)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'products/{new_filename}/{final_filename}'

class ProductManager(models.Manager):
    def feautured(self):
        return self.get_queryset().filter(feautured=True)

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None


class Product(models.Model):
    title           = models.CharField(max_length = 30)
    slug            = models.SlugField(default="abc", unique=True)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=10, default=39.99)
    image           = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    feautured       = models.BooleanField(default=False)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug" : self.slug})

    def __str__(self):
        return self.title

    objects = ProductManager()

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = 'abc'

pre_save.connect(product_pre_save_receiver, sender=Product)