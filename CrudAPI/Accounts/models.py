from django.db import models

class Admin(models.Model):
    AdminID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=15)
    Password = models.CharField(max_length=30)
    
    class Meta:
        db_table = '[Person].[Admin]'
        managed = False