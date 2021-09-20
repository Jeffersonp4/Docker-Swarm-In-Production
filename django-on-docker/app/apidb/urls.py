from django.urls import path
from apidb.api import conex_api_view,fiel_connex_detail_view,TableView,TableCrud

urlpatterns = [
    path('conexiones/', conex_api_view, name = 'conexion_api'),
    path('tableView',TableView, name = 'TableView' ),
    path('conexiones/<int:pk>/',fiel_connex_detail_view, name = 'conex_detail_api_view'),
    path('tableView/<int:pk>/',TableCrud, name = 'TableCrud')
]