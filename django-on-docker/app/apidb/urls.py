from django.urls import path
from apidb.api import ConexAPIView

urlpatterns = [
    path('conexiones/', ConexAPIView.as_view(), name = 'conexion_api')
]