from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import *
from .models import *

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return (permissions.AllowAny(),)
        return (permissions.IsAdminUser(),)
