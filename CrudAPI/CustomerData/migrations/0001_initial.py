# Generated by Django 5.0.10 on 2024-12-27 04:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('AddressID', models.AutoField(primary_key=True, serialize=False)),
                ('AddressLine1', models.CharField(max_length=60)),
                ('City', models.CharField(max_length=30)),
                ('StateProvinceID', models.IntegerField()),
                ('PostalCode', models.CharField(max_length=15)),
            ],
            options={
                'db_table': '[Person].[Address]',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AddressType',
            fields=[
                ('AddressTypeID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': '[Person].[AddressType]',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BusinessEntity',
            fields=[
                ('BusinessEntityID', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': '[Person].[BusinessEntity]',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CountryRegion',
            fields=[
                ('CountryRegionCode', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': '[Person].[CountryRegion]',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmailAddress',
            fields=[
                ('EmailAddressID', models.AutoField(primary_key=True, serialize=False)),
                ('EmailAddress', models.CharField(max_length=50)),
                ('BusinessEntityID', models.ForeignKey(to='CustomerData.businessentity', unique=True, on_delete=django.db.models.deletion.CASCADE, db_column='BusinessEntityID')),
            ],
            options={
                'db_table': '[Person].[EmailAddress]',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StateProvince',
            fields=[
                ('StateProvinceID', models.AutoField(primary_key=True, serialize=False)),
                ('StateProvinceCode', models.CharField(max_length=3)),
                ('CountryRegionCode', models.CharField(max_length=3)),
                ('Name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': '[Person].[StateProvince]',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('BusinessEntityID', models.ForeignKey(db_column='BusinessEntityID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='CustomerData.emailaddress', unique=True)),
                ('PersonType', models.CharField(max_length=2)),
                ('NameStyle', models.BooleanField()),
                ('Title', models.CharField(max_length=8, null=True)),
                ('FirstName', models.CharField(max_length=50)),
                ('MiddleName', models.CharField(max_length=50, null=True)),
                ('LastName', models.CharField(max_length=50)),
                ('Suffix', models.CharField(max_length=10, null=True)),
                ('EmailPromotion', models.IntegerField()),
                ('AdditionalContactInfo', models.TextField(null=True)),
                ('Demographics', models.TextField(null=True)),
            ],
            options={
                'db_table': '[Person].[Person]',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BusinessEntityAddress',
            fields=[
                ('BusinessEntityID', models.ForeignKey(db_column='BusinessEntityID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='CustomerData.person', unique=True)),
            ],
            options={
                'db_table': '[Person].[BusinessEntityAddress]',
                'managed': False,
            },
        ),
    ]
