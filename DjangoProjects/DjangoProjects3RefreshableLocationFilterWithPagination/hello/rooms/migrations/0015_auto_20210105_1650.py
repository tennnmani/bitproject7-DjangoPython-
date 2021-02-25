# Generated by Django 3.1.4 on 2021-01-05 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0014_auto_20210105_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='rooms.city'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='location',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, to='rooms.location'),
            preserve_default=False,
        ),
    ]