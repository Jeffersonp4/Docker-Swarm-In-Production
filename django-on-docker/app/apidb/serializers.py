from rest_framework import serializers
from class_field.models import conexs_pool_field

# Create your views here.
class classFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = conexs_pool_field
        fields = '__all__'
