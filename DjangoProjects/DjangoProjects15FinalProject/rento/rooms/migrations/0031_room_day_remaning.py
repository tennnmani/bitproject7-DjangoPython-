# Generated by Django 3.1.5 on 2021-01-18 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0030_auto_20210118_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='day_remaning',
            field=models.IntegerField(default=0),
        ),
    ]