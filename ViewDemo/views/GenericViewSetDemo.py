from rest_framework.viewsets import GenericViewSet
from ViewDemo.models import User
from ViewDemo.serializers import UserModelSerializer
from rest_framework.response import Response


class UserGenericViewSet(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def list(self, request):
        print(request.query_params)
        users = self.get_queryset()
        ser = self.get_serializer(users, many=True)
        return Response({'data': ser.data, 'message': 'success'})

    def retrieve(self, request, pk):
        print(request.query_params)
        try:
            user = self.get_object()
        except Exception as e:
            return Response({'message': str(e)})
        ser = self.get_serializer(user)
        return Response({'data': ser.data, 'message': 'success'})

    def create(self, request):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({'data': ser.data, 'message': 'success'})

    def destroy(self, request, pk):
        print(request.data)
        try:
            user = self.get_object()
        except Exception as e:
            return Response({'message': str(e)})
        user.delete()
        return Response({'message': 'success'})
