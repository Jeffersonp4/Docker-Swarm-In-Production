from rest_framework.response import Response
from rest_framework.views import APIView
from apidb.serializers import classFieldSerializer
from class_field.models import conexs_pool_field

class ConexAPIView(APIView):

    def get(self,request):
        field_connex = conexs_pool_field.objects.all()
        json_serializer = classFieldSerializer(field_connex,many= True)
        return Response(json_serializer.data)
