from django.db import models
from .Person import Person
from .Address import Address
from .AddressType import AddressType

class BusinessEntityAddress(models.Model):
    BusinessEntityID = models.ForeignKey(Person, unique=True, primary_key=True, on_delete=models.CASCADE, db_column='BusinessEntityID')
    AddressID = models.ForeignKey(Address, on_delete=models.CASCADE, db_column='AddressID')
    AddressTypeID = models.ForeignKey(AddressType, on_delete=models.CASCADE, db_column='AddressTypeID')
    class Meta:
        db_table = '[Person].[BusinessEntityAddress]'
        managed = False