# Generated by Django 3.2.6 on 2021-08-30 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210830_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuesta',
            name='votos',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]