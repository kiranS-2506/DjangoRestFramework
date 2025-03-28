import io
from django.views.generic import View
from rest_framework.parsers import JSONParser
from api.models import employee
from api.serializers import employeeSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
class EmployeeCRUDCBV(View):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id',None)
        if id:
            emp = employee.objects.get(id=id)
            eserializer = employeeSerializer(emp)
            json_data = JSONRenderer().render(eserializer.data)
            return HttpResponse(json_data,content_type='application/json',status=200)
        else:
            qs = employee.objects.all()
            eserializer = employeeSerializer(qs,many=True)
            json_data = JSONRenderer().render(eserializer.data)
            return HttpResponse(json_data,content_type='application/json')



