# Generated by Django 2.0.2 on 2018-02-10 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gorgonzola_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
