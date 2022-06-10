from rest_framework.generics import GenericAPIView
from ViewDemo.models import User
from ViewDemo.serializers import UserModelSerializer
from rest_framework.response import Response


class UsersGenericAPIView(GenericAPIView):
    # 指定 queryset
    queryset = User.objects.all()
    # 指定 serializer
    serializer_class = UserModelSerializer

    # 指定分页器
    # pagination_class = None
    # 指定过滤器
    # filter_backends = None
    # 查询单一数据库对象时使用的条件字段，默认为'pk'
    # lookup_field
    # 查询单一数据时URL中的参数关键字名称，默认与look_field相同
    # lookup_url_kwarg
    def get(self, request):
        users = self.get_queryset()
        ser = self.get_serializer(users, many=True)
        return Response({'data': ser.data, 'message': 'success'})

    def post(self, request):
        data = request.data
        ser = self.get_serializer(data=data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({'data': ser.data, 'message': 'success'})


class UserGenericAPIView(GenericAPIView):
    # 指定 queryset
    queryset = User.objects.all()
    # 指定 serializer
    serializer_class = UserModelSerializer

    def get(self, request, pk):
        try:
            # 从queryset中获取当前pk所对应的数据对象
            user = self.get_object()
        except Exception as e:
            return Response({'message': str(e)})
        ser = self.get_serializer(user)
        return Response({'data': ser.data, 'message': 'success'})

    def put(self, request, pk):
        try:
            book = self.get_object()
        except Exception as e:
            return Response({'message': str(e)})
        ser = self.get_serializer(book, data=request.data)
        # is_valid是序列化器的验证方法
        # raise_exception=True 验证失败直接返回
        ser.is_valid(raise_exception=True)
        # 更新数据
        ser.save()
        # 返回保存后的数据
        return Response({'data': ser.data, 'message': 'success'})

    def delete(self, request, pk):
        try:
            book = self.get_object()
        except Exception as e:
            return Response({'message': str(e)})
        book.delete()
        return Response({'message': 'success'})
