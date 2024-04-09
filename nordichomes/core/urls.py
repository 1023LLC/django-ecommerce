from django.urls import path

from . import views



app_name = 'core'



urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('shop/', views.shop, name='shop'),
]