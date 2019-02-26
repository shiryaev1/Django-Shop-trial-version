from django.shortcuts import render
from .forms import SubscribersForm
from products.models import *


def landing(request):
    form = SubscribersForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_form = form.save()
    return render(request, 'landing/landing.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True,is_main=True)
    products_images_phones = products_images.filter(product__category_id=1)
    products_images_laptops = products_images.filter(product__category_id=2)

    return  render(request, 'landing/home.html',locals())