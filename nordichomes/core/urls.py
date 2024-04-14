from django.urls import path

from .views import frontpage, shop, signup, myaccount

from django.contrib.auth import views


app_name = 'core'



urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('myaccount/', myaccount, name='myaccount'),
    path('shop/', shop, name='shop'),
]