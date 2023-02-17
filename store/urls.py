from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('products/', views.products, name='products'),
    path('add-product/', views.add_product,name='add'),
]
