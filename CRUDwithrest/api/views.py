import io
from django.views.generic import View
from rest_framework.parsers import JSONParser
from api.models import employee
from api.serializers import employeeSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt,name='dispatch')
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
    def post(self,request,*args,**kwrgs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        serializer = employeeSerializer(data=pdata)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg':'Resource created successfully....'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type='application/json',status=400)
    def put(self,request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id')
        emp = employee.objects.get(id=id)
        serilizer = employeeSerializer(emp,data=pdata,partial=True)
        if serilizer.is_valid():
            serilizer.save()
            
            msg = {'msg':"record updated"}
            jsaon_data= JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json")

        else:
            json_data=JSONRenderer().render(serilizer.errors)
            return HttpResponse(json_data,content_type="application/json", status=400)
    def delete(self,request):
        json_data = request.body
        stream =io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id')
        emp = employee.objects.get(id=id)
        emp.delete()
        msg={'msg':"record deleted"}
        return HttpResponse(JSONRenderer().render(msg),content_type='application/json')
    







