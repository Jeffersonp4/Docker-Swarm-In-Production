import psycopg2
from django.shortcuts import render, get_object_or_404, redirect
import logging
import mysql.connector as sql
import pyodbc
# Create your views here.
from class_field.forms import connex_Form
from class_field.models import conexs_pool_field
from django.contrib import messages

from django.shortcuts import redirect


def test_connections(request,connex):
    try:

        if connex.db_type == 'Posgresql':
            conn = psycopg2.connect(
                host=connex.ip,
                database=connex.db_name,
                user=connex.user,
                password=connex.pwd,
                port=connex.puerto
            )
            messages.success(request, f'The connection was successfully registered: {conn}')

        elif connex.db_type == 'Mysql':
            conMysql = sql.connect(
                host=connex.ip,
                database=connex.db_name,
                user=connex.user,
                passwd=connex.pwd,
                port=connex.puerto
            )
            messages.success(request, f'The connection was successfully registered: {conMysql}')

        elif connex.db_type == 'SqlServer':
            conn = pyodbc.connect(
                f'DRIVER=FreeTDS;SERVER={connex.ip};DATABASE={connex.db_name};UID={connex.user};PWD={connex.pwd};PORT={connex.puerto}')
            messages.success(request, f'The connection was successfully registered: {conn}')
    except:
        messages.success(request, f'The connection to the database could not be established')