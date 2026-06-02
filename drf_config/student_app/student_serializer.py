from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

    def validate_name(self,value):

        data=Student.objects.filter(name=value)
        if data.exists():
            raise serializers.ValidationError("Name is already Exists.")
        return value

    def validate_phone(self,value):
        data=Student.objects.filter(phone=value)
        if data.exists():
            raise serializers.ValidationError("phone number already exists")
        if not value.startswith('+91'):
            raise serializers.ValidationError("start phone number with +91")
        return value


from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']

    extra_kwargs = {
        'password': {'write_only': True}
    }

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )

        return user


from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
