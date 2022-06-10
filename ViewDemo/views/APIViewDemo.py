from rest_framework.response import Response
from rest_framework.views import APIView
from ViewDemo.models import User
from ViewDemo.serializers import UserModelSerializer


class UserListView(APIView):
    @staticmethod
    def get(request):
        users = User.objects.all()
        serializer = UserModelSerializer(users, many=True)
        return Response({'data': serializer.data, 'message': 'success'})

    @staticmethod
    def post(request):
        serializer = UserModelSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response({'data': serializer.data, 'message': 'success'})


class UserDetailView(APIView):
    @staticmethod
    def get(request, pk):
        users = User.objects.filter(id=pk).first()
        serializer = UserModelSerializer(users)
        return Response({'data': serializer.data, 'message': 'success'})

    @staticmethod
    def put(request, pk):
        user = User.objects.filter(id=pk).first()
        serializer = UserModelSerializer(instance=user, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response({'data': serializer.data, 'message': 'success'})

    @staticmethod
    def delete(request, pk):
        user = User.objects.filter(id=pk).first()
        user.delete()
        return Response({'message': 'success'})
