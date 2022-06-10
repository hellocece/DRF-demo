from rest_framework.viewsets import ModelViewSet
from ViewDemo.models import User
from ViewDemo.serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
