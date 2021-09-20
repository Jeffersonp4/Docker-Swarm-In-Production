from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from apidb.serializers import classFieldSerializer,JsonTableSerializer
from class_field.models import conexs_pool_field,RelationshipBetweenTableConnections


# http://localhost:8000/conexiones/conexiones/
@api_view(['GET', 'POST'])
def conex_api_view(request):
    if request.method == 'GET':
        field_connex = conexs_pool_field.objects.all()
        json_serializer = classFieldSerializer(field_connex, many=True)
        return Response(json_serializer.data,status= status.HTTP_200_OK)
    elif request.method == 'POST':
        json_serializer = classFieldSerializer(data=request.data)
        if json_serializer.is_valid():
            json_serializer.save()
            return Response(json_serializer.data, status= status.HTTP_201_CREATED)
        return Response(json_serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT','DELETE'])
def fiel_connex_detail_view(request, pk=None):
    field_connex = conexs_pool_field.objects.filter(id=pk).first()

    if field_connex:

        if request.method == 'GET':
            json_serializer = classFieldSerializer(field_connex)
            return Response(json_serializer.data , status= status.HTTP_200_OK)

        elif request.method == 'PUT':
            json_serializer = classFieldSerializer(field_connex,data= request.data)

            if json_serializer.is_valid():
                json_serializer.save()
                return Response(json_serializer.data, status = status.HTTP_200_OK)

            return Response(json_serializer.errors, status= status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            field_connex.delete()
            return Response({'message': 'Connection successfully removed'}, status= status.HTTP_202_ACCEPTED)

    return Response({'message': 'The connection to this data has not been found'}, status = status.HTTP_400_BAD_REQUEST)


# Url http://localhost:8000/tableView/tableView
@api_view(['GET','POST'])
def TableView(request):
    if request.method == 'GET':
        field_table = RelationshipBetweenTableConnections.objects.all()
        json_serializer = JsonTableSerializer(field_table, many=True)
        return Response(json_serializer.data,status= status.HTTP_200_OK)
    elif request.method == 'POST':
        json_serializer = JsonTableSerializer(data=request.data)
        if json_serializer.is_valid():
            json_serializer.save()
            return Response(json_serializer.data, status= status.HTTP_201_CREATED)
        return Response(json_serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def TableCrud(request,pk=None):
    field_table = RelationshipBetweenTableConnections.objects.filter(id=pk).first()

    if field_table:

        if request.method == 'GET':
            json_serializer = JsonTableSerializer(field_table)
            return Response(json_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            json_serializer = JsonTableSerializer(field_table, data=request.data)

            if json_serializer.is_valid():
                json_serializer.save()
                return Response(json_serializer.data, status=status.HTTP_200_OK)

            return Response(json_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            field_table.delete()
            return Response({'message': 'Table successfully removed'}, status=status.HTTP_202_ACCEPTED)

    return Response({'message': 'The Table to this data has not been found'}, status=status.HTTP_400_BAD_REQUEST)





