# Generated by Django 2.2 on 2020-06-16 11:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0017_auto_20200616_1714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leavereportemployee',
            old_name='leave_date',
            new_name='from_leave_date',
        ),
        migrations.AddField(
            model_name='leavereportemployee',
            name='to_leave_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]