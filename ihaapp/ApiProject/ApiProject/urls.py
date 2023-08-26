"""
URL configuration for ApiProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from IhaKiralama import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", views.user_register, name="register"),
    path("login/", views.user_login, name="login"),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("logout_user", views.logout_user, name="logout"),
    re_path(r'^',include('IhaKiralama.urls')),
    path('iha-list/', views.all_iha_list, name='iha-list'),
  
    path('kira-list/', views.all_kira_list, name='kira-list'),
     path('user-list/', views.all_user_list, name='user-list'),
   
    path('user-kiralama/', views.user_kira_list, name='user-kiralama'),



]
