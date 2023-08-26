from django.urls import path,include
from IhaKiralama import views

from rest_framework.routers import DefaultRouter
from .views import IHAViewSet,KiraViewSet,UserViewSet

router = DefaultRouter()
router.register(r'iha', IHAViewSet)
router.register(r'kirala', KiraViewSet)
router.register(r'users', UserViewSet)
urlpatterns = [
    
    path('api/', include(router.urls)),
]



#Api Linkleri

# urlpatterns=[
#     re_path(r'^iha$',views.ihaApi),
#     re_path(r'^iha/([0-9]+)$',views.ihaApi),

#     re_path(r'^kiralama$',views.kiralamaApi),
#     re_path(r'^kiralama/([0-9]+)$',views.kiralamaApi),

# ]



