from django.shortcuts import render, redirect
from app.models import DogProduct, Purchase, DogTag
from datetime import datetime
from django.contrib import messages
from app.forms import NewDogTagForm


def home(request):
    dog_products = DogProduct.objects.all()
    return render(request, "home.html", {"dog_products": dog_products})


def dog_product_detail(request, dog_product_id):
    dog_product = DogProduct.objects.get(id=dog_product_id)
    return render(request, "dog_product_detail.html", {"dog_product": dog_product})


def purchase_dog_product(request, dog_product_id):
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


def purchase_detail(request, purchase_id):
    purchase = Purchase.objects.get(id=purchase_id)
    return render(request, "purchase_detail.html", {"purchase": purchase})


def new_dog_tag(request):
    if request.method == "GET":
        return render(request, "new_dog_tag.html")
    else:
        form = NewDogTagForm(request.POST)
        if form.is_valid():
            owner_name = form.cleaned_data["owner_name"]
            dog_name = form.cleaned_data["dog_name"]
            dog_birthday = form.cleaned_data["dog_birthday"]
            dog_tag_color = form.cleaned_data["dog_tag_color"]
            new_tag = DogTag.objects.create(
                owner_name=owner_name,
                dog_name=dog_name,
                dog_birthday=dog_birthday,
                dog_tag_color=dog_tag_color,
            )
            new_tag.save()
            return redirect("dog_tag_list")
        else:
            form = NewDogTagForm()
            return render(request, "new_dog_tag.html", {"form": form})


def dog_tag_list(request):
    dogtags = DogTag.objects.all()
    return render(request, "dog_tag_list.html", {"dog_tags": dogtags})


def dog_tag_templates(request):
    pass
