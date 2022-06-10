from rest_framework import serializers
from SerializerDemo.models import Student
from SerializerDemo.models import Teacher


def check_sex(value):
    """
    外部校验器 validator
    """
    if value not in [0, 1, 2]:
        raise serializers.ValidationError(
            detail='性别设置错误',
            code='check_sex'
        )
    return value


class StudentSerializer(serializers.Serializer):
    """
    完整的序列化类内部包含三部分的内容
    1、序列化转换的字段声明
    2、反序列化的校验器，即校验前端传入的字段
    3、反序列化模型操作的方法，create和update方法
    """
    # read_only=True,在客户端提交数据[反序列化阶段]不要求ID字段
    id = serializers.IntegerField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    # required=True,反序列化阶段必填
    name = serializers.CharField(required=True)
    # 最大值 max_value 和最小值 min_value
    age = serializers.IntegerField(
        max_value=100,
        min_value=0,
        error_messages={
            "min_value": "Age must older than 0",
            "max_value": "Age must younger than 100"
        }
    )
    # 默认值为 True
    active = serializers.BooleanField(default=True)
    # validator的值为列表，列表的成员为函数名，而不是函数的调用
    sex = serializers.IntegerField(validators=[check_sex])
    # 允许客户端不填写内容（None）,或者值为 ""
    description = serializers.CharField(allow_null=True, allow_blank=True)

    def validate_name(self, data):
        """
        校验单个字段
        方法名必须以validate_<字段名>为名称，否则序列化器无法识别
        validate开头的方法，会自动被is_valid调用
        """
        if data in ["管理员", "超级管理员"]:
            raise serializers.ValidationError(
                detail="学生名字不能是管理员或者超级管理员",
                code="name"
            )

        return data

    # 全局钩子
    def validate(self, attrs):
        """
        验证来自客户端的所有字段
        """
        if not attrs['active'] and attrs['description']:
            raise serializers.ValidationError(
                detail='非active学生需要添加描述',
                code='validate'
            )
        return attrs

    def update(self, instance, validated_data):
        """
        参数都是固定的，
        instance 实例化序列化器对象时，必须要传入的模型对象
        """
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def create(self, validated_data):
        """
        保存数据
        """
        return Student.objects.create(**validated_data)


class TeacherModelSerializer(serializers.ModelSerializer):
    class Meta:
        # 1、指定对应的 Django 模型，必填
        model = Teacher
        # 2、声明转换字段必填，如果需要全部转换可以设置为 __all__
        # fields = '__all__'
        fields = ['id', 'name', 'age', 'sex', 'date_joined', 'active']
        # read_only_fields指明只读字段，即仅用于序列化输出的字段
        read_only_fields = ['id', 'date_joined']
        # 也可以使用exclude可以明确排除掉哪些字段
        # exclude = ['id']
        # 字段额外选项信息，如错误的提示信息，选填
        extra_kwargs = {
            "name": {
                'required': True
            },
            "age": {
                "max_value": 60,
                "min_value": 5,
                "error_messages": {
                    "max_value": "must younger than 60",
                    "min_value": "must older than 5",
                }
            }
        }

    # 全局钩子
    def validate(self, attrs):
        """
        验证来自客户端的所有字段
        """
        if not attrs['active'] and attrs['description']:
            raise serializers.ValidationError(
                detail='非active老师需要添加描述',
                code='validate'
            )
        return attrs
