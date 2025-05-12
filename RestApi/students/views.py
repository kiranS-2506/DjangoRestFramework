from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def student_details(request):
    data = [
        {
            'id':1,
            'name':'kiran',
            'age':23
        }
    ]
    return HttpResponse(data)
    