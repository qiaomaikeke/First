# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.db import models

# Create your models here.
#会员名单
class VIP(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name
