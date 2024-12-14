from django.db import models

class CustomerDemographics(models.Model):
    CustomerDemographicsID = models.IntegerField(primary_key=True)
    PersonType = models.CharField(max_length=2)
    TotalPurchaseYTD = models.DecimalField(max_digits=10, decimal_places=2)
    BirthDate = models.DateTimeField()
    MaritalStatus = models.CharField(max_length=1)
    YearlyIncome = models.CharField(max_length=30)
    Gender = models.CharField(max_length=1)
    TotalChildren = models.IntegerField()
    NumberChildrenAtHome = models.IntegerField()
    Education = models.CharField(max_length=30)
    Occupation = models.CharField(max_length=30)
    HomeOwnerFlag = models.BooleanField()
    NumberCarsOwned = models.IntegerField()
