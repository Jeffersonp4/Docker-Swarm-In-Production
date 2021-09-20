"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from Sync_Management.views import show_database, select_table
from apidb import views
from class_field.views import details_conex, Add_connex, edit_conex, delet_connex, test_connection, AddTable, EdiTable, \
    DeleteTable
from pool_view_connection.views import bienvenido, menu, ViewTable
from upload.views import image_upload

# router = routers.DefaultRouter()
# router.register(r'conexs_pool_field', views.conexs_pool_fieldViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", image_upload, name="upload"),
    path("", menu, name='IndexGeneral'),
    path("Index", bienvenido, name='Index'),
    path("IndexTable",ViewTable, name='IndexTable'),
    path('details_connex/<int:id>', details_conex),
    path('Add_connex', Add_connex),
    path('Add_Table', AddTable),
    path('edit_connex/<int:id>', edit_conex),
    path('editTable/<int:id>',EdiTable),
    path('DeleteTable/<int:id>', DeleteTable),
    path('delet_connex/<int:id>', delet_connex),
    path('Sync', show_database, name='Sync'),
    path('select_table/<int:id>', select_table),
    path('test_connection/<int:id>', test_connection),
    path('conexiones/', include('apidb.urls')),
    path('tableView/', include('apidb.urls'))

]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
