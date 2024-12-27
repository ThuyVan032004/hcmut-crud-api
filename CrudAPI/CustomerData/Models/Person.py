from django.db import models
from .BusinessEntity import BusinessEntity

class Person(models.Model):
    BusinessEntityID = models.ForeignKey(BusinessEntity, unique=True, on_delete=models.CASCADE, primary_key=True, db_column='BusinessEntityID')
    PersonType = models.CharField(max_length=2)
    NameStyle = models.BooleanField()
    Title = models.CharField(max_length=8, null=True)
    FirstName = models.CharField(max_length=50)
    MiddleName = models.CharField(max_length=50, null=True)
    LastName = models.CharField(max_length=50)
    Suffix = models.CharField(max_length=10, null=True)
    EmailPromotion = models.IntegerField()
    AdditionalContactInfo = models.TextField(null=True)
    Demographics = models.TextField(null=True)
    class Meta:
        db_table = '[Person].[Person]'
        managed = False