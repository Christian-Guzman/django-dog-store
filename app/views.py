from django.shortcuts import render, redirect
from app.models import DogProduct, Purchase, DogTag
from datetime import datetime
from django.contrib import messages
from app.forms import NewDogTagForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, View, CreateView


class DogProductList(ListView):
    model = DogProduct
    context_object_name = "dog_products"
    template_name = "home.html"


class DogProductDetail(DetailView):
    model = DogProduct
    context_object_name = "dog_product"
    template_name = "dog_product_detail.html"
    pk_url_kwarg = "dog_product_id"


class PurchaseDogProduct(View):
    def post(self, request, dog_product_id):
        dog_product = DogProduct.objects.get(id=dog_product_id)
        if dog_product.quantity > 0:
            dog_product.quantity -= 1
            new_purchase = dog_product.purchase_set.create(purchased_at=datetime.now())
            messages.success(request, f"Purchased {dog_product.name}")
            dog_product.save()
            return redirect("purchase_detail", new_purchase.id)
        elif dog_product.quantity == 0:
            messages.error(request, f"{dog_product.name} is out of stock")
            return redirect("dog_product_detail", dog_product.id)



class PurchaseDetail(DetailView):
    model = Purchase
    context_object_name = "purchase"
    template_name = "purchase_detail.html"
    pk_url_kwarg = "purchase_id"



class NewDogTag(CreateView):
    model = DogTag
    fields = ['owner_name', 'dog_name', 'dog_birthday', 'dog_tag_color']
    success_url = reverse_lazy('dog_tag_list')
    template_name = 'new_dog_tag.html'
    context_object_name = 'form'


class DogTagList(ListView):
    model = DogTag
    template_name = 'dog_tag_list.html'
    context_object_name = 'dog_tags'

