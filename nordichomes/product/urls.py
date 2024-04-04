from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('shop/<slug:slug>/', views.product, name='product')
]