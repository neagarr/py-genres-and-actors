# Generated by Django 5.1rc1 on 2024-08-01 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='first_name',
            field=models.CharField(max_length=256),
        ),
    ]