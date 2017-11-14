# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    template_name = "index.html"
    context = {}
    return render(request, template_name, context)

def dashboard(request):
    template_name = "dashboard_user.html"
    context = {}
    return render(request,template_name,context)