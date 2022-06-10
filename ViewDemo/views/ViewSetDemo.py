from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from ViewDemo.models import User
from ViewDemo.serializers import UserModelSerializer


class UserViewSet(ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = User.objects.all()  # 不在类内定义 queryset,需要在路由中设置 basename

    def list(self, request):
        serializer = UserModelSerializer(self.queryset, many=True)
        return Response({'data': serializer.data, 'message': 'success'})

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = UserModelSerializer(user)
        return Response({'data': serializer.data, 'message': 'success'})
