# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import HeroSerializer,AddressSerializer
from .models import Hero,Address


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class AddressViewSet(viewsets.ModelViewSet):
	queryset = Address.objects.all().order_by('zip')
	serializer_class = AddressSerializer