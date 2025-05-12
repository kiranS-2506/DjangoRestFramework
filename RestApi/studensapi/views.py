# from django.shortcuts import render
#from django.http import JsonResponse
from studensapi.models import student
from .seriallizers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def students(request):
    if request.method == "GET":
        stud_data = student.objects.all()
        serializer = StudentSerializer(stud_data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def student_data(request,pk):
    try:
        student_details = student.objects.get(pk=pk)
        print(student_details)
    except student.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serilizer = StudentSerializer(student_details)
        return Response(serilizer.data,status = status.HTTP_200_OK)