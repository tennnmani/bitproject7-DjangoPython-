# Generated by Django 3.1.4 on 2021-01-04 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_auto_20210104_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]