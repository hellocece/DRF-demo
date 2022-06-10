from rest_framework import serializers
from ViewDemo.models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
