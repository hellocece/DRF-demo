from rest_framework.views import APIView
from django.http import JsonResponse
from SerializerDemo.models import Student
from SerializerDemo.serializers import StudentSerializer
import json


# Create your views here.


class StudentView(APIView):
    def get(self, request, pk):
        """
        序列化器，序列化阶段的调用
        """
        if pk == 'all':
            # 1、获取数据集
            student_list = Student.objects.all()
            # 2、实例化序列化器，得到序列化对象
            serializer = StudentSerializer(instance=student_list, many=True)
            # 3、调用序列化对象的data属性方法获取转换后的数据
            data = serializer.data
            # 4、响应数据
            return JsonResponse({'data': data, 'message': 'success'})
        else:
            query = Student.objects.filter(id=pk)
            if query.count():
                student = query.first()
                serializer = StudentSerializer(instance=student)
                data = serializer.data
                return JsonResponse({'data': data, 'message': 'success'})
            else:
                return JsonResponse({'message': 'ID不存在'})

    def post(self, request, pk):
        """反序列化，采用字段选项来验证数据"""
        # 1、接收客户端提交的数据
        # 1.1 实例化序列化器，获取序列化对象
        data = request.data
        # 1.2 调用序列化对象验证数据
        serializer = StudentSerializer(data=data)
        # 1.3 获取验证结果
        serializer.is_valid()  # 不抛出异常
        serializer.is_valid(raise_exception=True)  # 抛出异常
        # 2、操作数据
        serializer.save()
        # 3、返回数据
        return JsonResponse({'data': data, 'message': '添加成功'})

    def put(self, request, pk):
        """反序列化，采用字段选项来验证数据"""
        # 1、根据客户端提交的数据获取指定数据
        # 1.1 实例化序列化器，获取序列化对象
        pk = request.data.get('id', '')
        student = Student.objects.filter(id=pk).first()
        data = request.data
        # 1.2 调用序列化对象验证数据
        serializer = StudentSerializer(instance=student, data=data)
        # 1.3 获取验证结果
        serializer.is_valid(raise_exception=True)  # 抛出异常
        # 2、操作数据
        # 会根据实例化序列化器的时候是否传入instance属性来自动调用create或者update方法，如果传入instance属性，调用update方法，没有传入instance属性，调用create方法
        serializer.save()
        # 3、返回数据
        return JsonResponse({'data': data, 'message': '修改成功'})
