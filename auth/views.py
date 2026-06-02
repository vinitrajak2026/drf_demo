from django.shortcuts import render
from rest_framework import status

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .user_serializers import UserSerializer


@api_view(['POST'])
def register_user(request):
    try:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    except Exception as e:
        return Response(e)