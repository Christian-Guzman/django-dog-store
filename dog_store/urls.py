from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path(
        "dog-product/<dog_product_id>",
        views.dog_product_detail,
        name="dog_product_detail",
    ),
    path(
        "dog-product/<dog_product_id>/purchase",
        views.purchase_dog_product,
        name="purchase_dog_product",
    ),
    path("purchase/<purchase_id>", views.purchase_detail, name="purchase_detail"),
    path("dogtag/new", views.new_dog_tag, name="new_dog_tag"),
    path("dogtag", views.dog_tag_list, name="dog_tag_list"),
]
