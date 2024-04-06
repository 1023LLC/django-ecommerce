from django.urls import path

from . import views



app_name = 'core'



urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup', views.signup, name='signup'),
    path('shop/', views.shop, name='shop'),
]