# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Hero,Address

admin.site.register(Hero)
admin.site.register(Address)

# Register your models here.
