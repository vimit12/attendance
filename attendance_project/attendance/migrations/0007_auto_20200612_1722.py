# Generated by Django 2.2 on 2020-06-12 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0006_auto_20200612_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='out_time',
            field=models.TimeField(blank=True, default='', null=True),
        ),
    ]
