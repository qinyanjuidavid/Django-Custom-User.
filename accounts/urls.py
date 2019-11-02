from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_view
app_name="accounts"

urlpatterns=[
path('',auth_view.LoginView.as_view(template_name='accounts/login.html'),name='login'),
path('home/',views.home,name='home'),
path('register/',views.register,name='register'),
]
