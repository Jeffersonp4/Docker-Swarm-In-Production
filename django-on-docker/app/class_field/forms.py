import sys
from psycopg2 import pool
from django.forms import *
import logging


from class_field.models import conexs_pool_field, RelationshipBetweenTableConnections


class connex_Form(ModelForm):

    class Meta:
        model = conexs_pool_field
        fields = '__all__'
        widgets = {

            'pwd': PasswordInput(attrs={'type': 'password'})
        }


class TableForm(ModelForm):

    class Meta:
        model = RelationshipBetweenTableConnections
        fields = '__all__'


class RelationTable(Form):
    conexs_pool_fields = ModelChoiceField(queryset=conexs_pool_field.objects.all(), widget=Select(attrs={
        'class': 'form-control'
    }))

    tables_fields = ModelChoiceField(queryset=RelationshipBetweenTableConnections.objects.none(), widget=Select(attrs={
        'class': 'form-control'
    }))
