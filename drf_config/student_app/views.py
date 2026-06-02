from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from .models import Student
from .student_serializer import StudentSerializer, UserSerializer, ProductSerializer
from rest_framework.authentication import BasicAuthentication

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.contrib.auth import authenticate,login,logout


# Create your views here.



@api_view(['POST','GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def student_view(request):
    if request.method=='POST':
        data=request.data
        student_serializer=StudentSerializer(data=data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data)
        else:
            return Response(student_serializer.errors)


@api_view(['PUT'])
def update_student(request,id):
    student_object=Student.objects.get(id=id)
    student_serializer=StudentSerializer(
       student_object,request.data
    )
    if student_serializer.is_valid():
        student_serializer.save()
        return Response({
            "message":"Student updated",
            "new Data": student_serializer.data
        })
    return Response(student_serializer.errors)



@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def user_operation(request):
    if request.method=="POST":
        userSerializer=UserSerializer(data=request.data)
        if userSerializer.is_valid():
            userSerializer.save()
            return Response(userSerializer.data)
    return Response(userSerializer.errors)



@api_view(['POST'])
def login_user(request):
    user_name=request.data.get("username")
    user_password=request.data.get("password")
    print(user_password)
    user=authenticate(
        username=user_name,
        password=user_password
    )
    if user is not None:
        login(request,user)
        return Response({"message":"login successfully"})
    return Response("please register")


@api_view(['POST'])
def create_product(request):

    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)



@api_view(['DELETE'])
def delete_by_id(request,id):
    """

    :param request:
    :param id:
    :return:
    """
    student_object=Student.objects.get(id=id)
    if student_object is not None:
        student_object.delete()
        return Response("Student deleted")
    return Response({
        "message":"Invalid Id Given"
    })
