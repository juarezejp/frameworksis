# Generated by Django 4.0.2 on 2022-02-24 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos',
            name='stock',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
