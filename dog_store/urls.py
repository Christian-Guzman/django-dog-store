from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.DogProductList.as_view(), name="home"),
    path(
        "dog-product/<dog_product_id>",
        views.DogProductDetail.as_view(),
        name="dog_product_detail",
    ),
    path(
        "dog-product/<dog_product_id>/purchase",
        views.PurchaseDogProduct.as_view(),
        name="purchase_dog_product",
    ),
    path(
        "purchase/<purchase_id>", views.PurchaseDetail.as_view(), name="purchase_detail"
    ),
    path("dogtag/new", views.NewDogTag.as_view(), name="new_dog_tag"),
    path("dogtag", views.DogTagList.as_view(), name="dog_tag_list"),
]
