from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json

# Create your views here.
def emp_data_json_view(request):
    emp_data ={
        'eno':102,
        'ename':'billgates',
        'esal':18000,
        'eaddr':'Vja'
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data)
def emp_data_json_view2(request):
        emp_data ={
        'eno':102,
        'ename':'elon musk',
        'esal':17000,
        'eaddr':'hyd'
    }
        return JsonResponse(emp_data)

    
        


