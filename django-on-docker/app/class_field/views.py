import psycopg2
from django.shortcuts import render, get_object_or_404, redirect
import logging
import mysql.connector as sql
import pyodbc
# Create your views here.
from class_field.forms import connex_Form, TableForm
from class_field.models import conexs_pool_field,RelationshipBetweenTableConnections
from class_field.test_conexs import test_connections
from django.contrib import messages

################### Connections ###################


def details_conex(request, id):
    # connex = conexs_pool.objects.get(pk=id)
    connex = get_object_or_404(conexs_pool_field, pk=id)
    return render(request, 'details.html', {'connex': connex})


# connex_Form = modelform_factory(conexs_pool, exclude=[])

def test_connection(request, id):
    connex = conexs_pool_field.objects.get(pk=id)
    if connex:
        test_connections(request,connex)
    else:
        messages.success(request, f'The connection to the database could not be established')
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


################### Tables ###################

def AddTable(request):
    if request.method == 'POST':
        formTable = TableForm(request.POST)
        if formTable.is_valid():
            formTable.save()
            return redirect('IndexTable')
    else:
        formTable = TableForm()

    return render(request, 'newsTable.html', {'formTable': formTable})

def EdiTable(request, id):
    connex = get_object_or_404(RelationshipBetweenTableConnections, pk=id)
    if request.method == 'POST':
        formTable = TableForm(request.POST, instance=connex)
        if formTable.is_valid():
            formTable.save()
            return redirect('IndexTable')
    else:
        formTable = TableForm(instance=connex)

    return render(request, 'editTable.html', {'formTable': formTable})

def DeleteTable(request, id):
    connex = get_object_or_404(RelationshipBetweenTableConnections, pk=id)
    if connex:
        connex.delete()
    return redirect('IndexTable')

################### Fields ###################
