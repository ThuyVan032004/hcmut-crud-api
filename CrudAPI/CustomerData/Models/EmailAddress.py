from django.db import models
from .BusinessEntity import BusinessEntity

class EmailAddress(models.Model):
    BusinessEntityID = models.ForeignKey(BusinessEntity, unique=True, on_delete=models.CASCADE, db_column='BusinessEntityID')
    EmailAddressID = models.AutoField(primary_key=True)
    EmailAddress = models.CharField(max_length=50)
    class Meta:
        db_table = '[Person].[EmailAddress]'
        managed = False