# Generated by Django 2.2 on 2020-06-14 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0012_auto_20200614_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceReportMonthly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('Jan', 'January'), ('Feb', 'Febuary'), ('Mar', 'March'), ('Apr', 'April'), ('May', 'May'), ('Jun', 'June'), ('Jul', 'July'), ('Aug', 'August'), ('Sep', 'September'), ('Oct', 'October'), ('Nov', 'November'), ('Dec', 'December')], default='Jan', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('attendance_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Attendance')),
                ('emp_id_report', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='attendance.Employee')),
            ],
        ),
        migrations.DeleteModel(
            name='AttendanceReport',
        ),
    ]
