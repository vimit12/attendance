# Generated by Django 2.2 on 2020-06-11 11:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_auto_20200611_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='in_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='out_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]