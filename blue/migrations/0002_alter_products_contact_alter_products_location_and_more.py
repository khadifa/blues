# Generated by Django 4.1.5 on 2023-01-31 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Contact',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='products',
            name='Location',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='products',
            name='Status',
            field=models.CharField(max_length=30),
        ),
    ]
