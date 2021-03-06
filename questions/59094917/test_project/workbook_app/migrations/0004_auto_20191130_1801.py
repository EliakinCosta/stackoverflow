# Generated by Django 2.2.7 on 2019-11-30 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workbook_app', '0003_auto_20191129_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='dept_name',
            field=models.CharField(default=1, max_length=40, verbose_name='dept_name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default=1, max_length=40, verbose_name='emp_id'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='hire_date',
            field=models.CharField(default=1, max_length=40, verbose_name='hire_date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='job_title',
            field=models.CharField(default=1, max_length=40, verbose_name='job_title'),
            preserve_default=False,
        ),
    ]
