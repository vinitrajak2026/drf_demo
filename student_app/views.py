from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from student_app.models import Student
from student_app.student_serializer import StudentSerializer


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
def student(request):
    if request.method == 'POST':
        data = request.data
        student_serializer = StudentSerializer(data=data, many=isinstance(data, list))
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data, status=status.HTTP_201_CREATED)
        return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        student_object = Student.objects.all()
        serializer = StudentSerializer(student_object, many=True)
        return Response(serializer.data)

    return Response({"message": f"Method {request.method} handled"}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_by_id(request, id):
    try:
        student_object = Student.objects.get(id=id)
        student_object.delete()
        return Response({"message": "Student deleted"}, status=status.HTTP_204_NO_CONTENT)
    except Student.DoesNotExist:
        return Response({"message": "Invalid id given"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_all_student(request):
    student_object = Student.objects.all()
    serializer = StudentSerializer(student_object, many=True)
    return Response(serializer.data)


@api_view(['PUT', 'PATCH'])
def update_student(request, id):
    try:
        student_obj = Student.objects.get(id=id)
        serializer = StudentSerializer(student_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student updated successfully", "data": serializer.data})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Student.DoesNotExist:
        return Response({"error": "Student not found!"}, status=status.HTTP_404_NOT_FOUND)