from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ,name="index"),
    path('product/', views.create_producto, name="producto"),
    path('purchase/', views.purchase, name="purchase"),
    path('pizza/', views.pizza, name="pizza"),
]
