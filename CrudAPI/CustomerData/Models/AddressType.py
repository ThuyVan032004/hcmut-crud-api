from django.db import models

class AddressType(models.Model):
    AddressTypeID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    class Meta:
        db_table = '[Person].[AddressType]'
        managed = False