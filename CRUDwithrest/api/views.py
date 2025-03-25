from django.shortcuts import render
from api.models import employee
from django.views.generic import View
from api.serializers import employeeSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.
class EmployeeCRUD(View):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream =io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id',None)
        if id is not None:
            emp = employee.objects.get(id=id)
            eserializer = employeeSerializer(emp)
            json_data = JSONRenderer().render(eserializer.data)
            return HttpResponse(json_data,content_type='application/json',status=200)
        qs = employee.objects.all()
        eserializer = employeeSerializer(qs,many=True)
        json_data = JSONRenderer().render(eserializer.data)
        return HttpResponse(json_data,content_type='application/json',status=200)



