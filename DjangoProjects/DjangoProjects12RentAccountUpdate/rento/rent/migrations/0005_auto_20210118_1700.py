# Generated by Django 3.1.4 on 2021-01-18 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0004_datetracker_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datetracker',
            name='date_updated',
            field=models.DateField(),
        ),
    ]