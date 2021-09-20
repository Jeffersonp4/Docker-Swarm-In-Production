from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from class_field.models import conexs_pool_field,RelationshipBetweenTableConnections


def bienvenido(request):
    no_conex = conexs_pool_field.objects.count()
    #connex = conexs_pool.objects.all()
    connex = conexs_pool_field.objects.order_by('id')
    return render(request , 'Index.html', {'no_conex': no_conex, 'connex':connex})


def menu(request):
    return render(request, 'IndexGeneral.html')

def ViewTable(request):
    connexTable = RelationshipBetweenTableConnections.objects.order_by('id')
    return render(request, 'IndexTable.html', {'connexTable':connexTable})