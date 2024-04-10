from django.urls import path

from .views import frontpage, shop, signup, login_old

from django.contrib.auth import views


app_name = 'core'



urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', login_old, name='login'),
    path('shop/', shop, name='shop'),
]