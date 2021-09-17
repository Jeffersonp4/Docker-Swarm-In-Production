import psycopg2
from django.shortcuts import render, get_object_or_404, redirect
from django.db import connection
from django.contrib import messages
# Create your views here.
from class_field.models import conexs_pool_field
import urllib, json

def show_database(request):
    #url = "http://localhost:8000/conexiones/conexiones/"
    #response = urllib.urlopen(url)
    #data = json.loads(response.read())
    peticion = conexs_pool_field.objects.all()
    return render(request, "Sync.html",{'peticion':peticion})


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
            return redirect('Sync.html')


def perfomSync(request):
    pass