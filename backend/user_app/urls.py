from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .views_auth import *

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', handle_login),
    path('logout/', handle_logout),
]