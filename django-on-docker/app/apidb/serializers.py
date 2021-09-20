from rest_framework import serializers
from class_field.models import conexs_pool_field, RelationshipBetweenTableConnections


# Create your views here.
class classFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = conexs_pool_field
        fields = '__all__'


class JsonTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelationshipBetweenTableConnections
        fields = '__all__'

    conexs_pool_id = classFieldSerializer()


