from django.urls import path
from . import views

urlpatterns = [
    path("health/", views.health, name="health"),
    path("", views.home, name="home"),
    path("shop/", views.shop, name="shop"),
    path("product/<int:pk>/", views.product, name="product"),
]
