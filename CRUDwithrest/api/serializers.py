from rest_framework import serializers
from api.models import employee
class employeeSerializer(serializers.Serializer):
    eno = serializers.IntegerField()
    ename = serializers.CharField(max_length=50)
    esal = serializers.FloatField()
    eadd = serializers.CharField(max_length=50)
    def create(self, validated_data):
        return employee.objects.create(**validated_data)
    def update(self,instance,data):
        instance.eno = data.get('eno',instance.eno)
        instance.ename = data.get('ename',instance.ename)
        instance.esal = data.get('esal',instance.esal)
        instance.eadd = data.get('eadd',instance.eadd)
        instance.save()
        return instance