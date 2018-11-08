from django.contrib import admin
from django.conf.urls import url, include

from . import views

urlpatterns = [
     url(r'^cap/$', views.cap, name='cap'),
     url(r'^glass/$', views.glass, name='glass'),
     url(r'^jackets/$', views.jackets, name='jackets'),
     url(r'^jeans/$', views.jeans, name='jeans'),
     url(r'^shoes/$', views.shoes, name='shoes'),
     url(r'^slippers/$', views.slippers, name='slippers'),
     url(r'^tshirt/$', views.tshirt, name='tshirt'),
     url(r'^watch/$', views.watch, name='watch'),
      	
]

