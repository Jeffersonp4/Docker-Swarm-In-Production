import sys
from psycopg2 import pool
from django.forms import ModelForm, PasswordInput
import logging

from class_field.models import conexs_pool_field
class connex_Form(ModelForm):

    class Meta:
        model = conexs_pool_field
        fields = '__all__'
        widgets = {

            'pwd': PasswordInput(attrs={'type': 'password'})
        }