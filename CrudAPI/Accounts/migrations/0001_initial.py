# Generated by Django 5.0.10 on 2024-12-30 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('AdminID', models.AutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=15)),
                ('Password', models.CharField(max_length=30)),
            ],
        ),
    ]