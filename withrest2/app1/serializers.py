from rest_framework.serializers import ModelSerializer
from app1.models import student

class studentSerializer(ModelSerializer):
    class Meta:
        model = student
        fields ='__all__'
