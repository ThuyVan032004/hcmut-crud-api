from django.db import models

class BusinessEntity(models.Model):
    BusinessEntityID = models.AutoField(primary_key=True)
    class Meta:
        db_table = '[Person].[BusinessEntity]'
        managed = False