# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    title           = models.CharField(max_length = 30)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=10, default=39.99)

    def __str__(self):
        return self.title