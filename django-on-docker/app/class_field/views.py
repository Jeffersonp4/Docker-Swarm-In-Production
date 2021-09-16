import psycopg2
from django.shortcuts import render, get_object_or_404, redirect
import logging
import mysql.connector as sql
import pyodbc
# Create your views here.
from class_field.forms import connex_Form
from class_field.models import conexs_pool_field
from django.contrib import messages


def details_conex(request, id):
    # connex = conexs_pool.objects.get(pk=id)
    connex = get_object_or_404(conexs_pool_field, pk=id)
    return render(request, 'details.html', {'connex': connex})


# connex_Form = modelform_factory(conexs_pool, exclude=[])

def test_connection(request, id):
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
            return redirect('Index')

        if connex.db_type == 'Mysql':
            conMysql = sql.connect(
                host=connex.ip,
                database=connex.db_name,
                user=connex.user,
                passwd=connex.pwd,
                port=connex.puerto
            )
            messages.success(request, f'La Conexion en mysql se registro correctamente: {conMysql}')
            return redirect('Index')

        if connex.db_type == 'SqlServer':
            conn = pyodbc.connect(f'DRIVER=FreeTDS;SERVER={connex.ip};DATABASE={connex.db_name};UID={connex.user};PWD={connex.pwd};PORT={connex.puerto}')
            messages.success(request, f'La Conexion en SqlServer ha sido exitosa : {conn}')
            return redirect('Index')


def Add_connex(request):
    if request.method == 'POST':
        formconnex = connex_Form(request.POST)
        if formconnex.is_valid():
            formconnex.save()
            return redirect('Index')
    else:
        formconnex = connex_Form()

    return render(request, 'news.html', {'formconnex': formconnex})

def edit_conex(request, id):
    connex = get_object_or_404(conexs_pool_field, pk=id)
    if request.method == 'POST':
        formconnex = connex_Form(request.POST, instance=connex)
        if formconnex.is_valid():
            formconnex.save()
            return redirect('Index')
    else:
        formconnex = connex_Form(instance=connex)

    return render(request, 'edit.html', {'formconnex': formconnex})


def delet_connex(request, id):
    connex = get_object_or_404(conexs_pool_field, pk=id)
    if connex:
        connex.delete()
    return redirect('Index')
