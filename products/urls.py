from django.contrib import admin
from django.urls import path,re_path
from products import views

urlpatterns = [
    re_path(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
]