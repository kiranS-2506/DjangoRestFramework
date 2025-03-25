from rest_framework import serializers
class employeeSerializer(serializers.Serializer):
    eno = serializers.IntegerField()
    ename = serializers.CharField(max_length=50)
    esal = serializers.FloatField()
    eadd = serializers.CharField(max_length=50)