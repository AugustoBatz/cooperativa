# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Asociado(models.Model):
    nombre = models.CharField(max_length=45, blank=False, null=False)
    apellido = models.CharField(max_length=45, blank=False, null=False)
    estado_civil = models.CharField(max_length=45, blank=False, null=False)
    telefono = models.CharField(max_length=45, blank=False, null=False)
    profesion = models.CharField(max_length=45, blank=False, null=False)
    trabajo = models.CharField(max_length=45, blank=False, null=False)
    direccion = models.CharField(max_length=100,blank=False,null=False)
    class Meta:
        managed = False
        db_table = 'Asociado'

