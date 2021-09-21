import psycopg2
import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.db import connection
from django.contrib import messages
# Create your views here.
from class_field.models import conexs_pool_field ,RelationshipBetweenTableConnections
from class_field.forms import RelationTable
import urllib, json

def show_database(request):
    #url = "http://localhost:8000/conexiones/conexiones/"
    #response = urllib.urlopen(url)
    #data = json.loads(response.read())
    #peticion = conexs_pool_field.objects.all()
    #return render(request, "Sync.html",{'peticion':peticion})


    #response = requests.get('http://localhost:8000/tableView/tableView')
    #datos_all = response.json()
    #db_name = datos_all
    conex_obj = RelationTable
    table_obj = RelationshipBetweenTableConnections.objects.order_by('id')

    return render(request,"Sync.html",{"conex_obj":conex_obj, "table_obj":table_obj})
 #for element in db_name:



def select_table(request,id):
    connex = conexs_pool_field.objects.get(pk=id)
    if connex:
        if connex.db_type == 'Posgresql':
            conn = psycopg2.connect(
                host=connex.ip,
                database=connex.db_name,
                user=connex.user,
                password=connex.pwd,
                port=connex.puerto
            )
            messages.success(request, f'La Conexion Se registro correctamente: {conn}')
            return redirect('Sync')


def perfomSync(request):
    pass