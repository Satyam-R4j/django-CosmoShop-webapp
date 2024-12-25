from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", views.index , name="shopHome"),
    path("about/", views.about, name="aboutUs"),
    path("tracker/",views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("productView/", views.productView, name="productView"),
    path("checkout/", views.checkout, name="checkout")
]
