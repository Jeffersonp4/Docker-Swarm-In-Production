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


class RelationshipBetweenTableConnections(models.Model):
    table = models.CharField(max_length=255)
    conexs_pool_id = models.ForeignKey(conexs_pool_field, on_delete=models.CASCADE)

class RelationshipBetweenTables(models.Model):
    fields = models.CharField(max_length=8000)
    table_id = models.ForeignKey(RelationshipBetweenTableConnections, on_delete=models.CASCADE)


class RelationshipBetweenConnections(models.Model):
    db_types = models.CharField(max_length=255)
    relations = models.ManyToManyField(conexs_pool_field)


class LinkBetweenTable(models.Model):
    tables = models.CharField(max_length=8000)
    link_connection = models.ForeignKey(RelationshipBetweenConnections, on_delete=models.CASCADE)

class LinkBetweenField(models.Model):
    Sync_type = models.CharField(max_length=255)
    relation_table = models.ForeignKey(LinkBetweenTable, on_delete=models.CASCADE)



