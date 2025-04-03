from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import studentSerializer
from .models import student
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


class studentlistview(APIView):
    def get(self,request):
        qs = student.objects.all()
        Serializer = studentSerializer(qs,many=True)
        return Response(Serializer.data)
    # Create your views here.

    def post(self,request):
        Serializer = studentSerializer(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)

