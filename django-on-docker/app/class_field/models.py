import sys
import logging
import psycopg2
from django.db import models
from psycopg2 import pool
# Create your models here.

db_types = [
    ('Posgresql', 'Posgresql'),
    ('Mysql', 'Mysql'),
    ('SqlServer', 'SqlServer')
]

class conexs_pool_field(models.Model):
    ip = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    pwd = models.CharField(max_length=255)
    db_name = models.CharField(max_length=255)
    db_type = models.CharField(max_length=255,
                               choices=db_types
                               )
    puerto = models.IntegerField()
    active = models.BooleanField()

    def __str__(self):
        return f'Conexion {self.id}: {self.ip}: {self.user}: {self.pwd}: {self.db_type}: {self.puerto}: {self.active}:'




