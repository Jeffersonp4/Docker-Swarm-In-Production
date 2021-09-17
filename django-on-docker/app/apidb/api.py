from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from apidb.serializers import classFieldSerializer
from class_field.models import conexs_pool_field


@api_view(['GET', 'POST'])
def conex_api_view(request):
    if request.method == 'GET':
        field_connex = conexs_pool_field.objects.all()
        json_serializer = classFieldSerializer(field_connex, many=True)
        return Response(json_serializer.data)
    elif request.method == 'POST':
        json_serializer = classFieldSerializer(data=request.data)
        if json_serializer.is_valid():
            json_serializer.save()
            return Response(json_serializer.data)
        return Response(json_serializer.errors)


@api_view(['GET'])
def fiel_connex_detail_view(request, pk=None):
    if request.method == 'GET':
        field_connex = conexs_pool_field.objects.filter(id=pk).first()
        json_serializer = classFieldSerializer(field_connex)
        return Response(json_serializer.data)
