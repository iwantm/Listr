# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class List(models.Model):
    task = models.CharField(max_length=200)
    date_due = models.DateTimeField()

    def __str__(self):
        return self.task
    
