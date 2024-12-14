# Generated by Django 5.0.10 on 2024-12-14 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManagementData', '0002_delete_customerdemographics'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDemographics',
            fields=[
                ('BusinessEntityID', models.IntegerField(primary_key=True, serialize=False)),
                ('PersonType', models.CharField(max_length=2)),
                ('TotalPurchaseYTD', models.DecimalField(decimal_places=2, max_digits=10)),
                ('BirthDate', models.DateTimeField()),
                ('MaritalStatus', models.CharField(max_length=1)),
                ('YearlyIncome', models.CharField(max_length=30)),
                ('Gender', models.CharField(max_length=1)),
                ('TotalChildren', models.IntegerField()),
                ('NumberChildrenAtHome', models.IntegerField()),
                ('Education', models.CharField(max_length=30)),
                ('Occupation', models.CharField(max_length=30)),
                ('HomeOwnerFlag', models.BooleanField()),
                ('NumberCarsOwned', models.IntegerField()),
            ],
        ),
    ]