# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.contrib import admin
#from django.conf.urls import include, url

# Create your views here.
admin.site.site_header = "Fleet Management"


def homepage(request):
    return render(request, "index.html")


def car_view(request):
    return render(request, "home.html")
