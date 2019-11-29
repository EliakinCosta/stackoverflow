# Generated by Django 2.2.7 on 2019-11-29 02:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workbook_app', '0002_auto_20191126_0247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, verbose_name='first name')),
                ('last_name', models.CharField(max_length=40, verbose_name='last name')),
                ('emp_photo', models.ImageField(upload_to='', verbose_name='passport')),
                ('date_of_birth', models.DateField(verbose_name='birthday')),
                ('house_address', models.CharField(max_length=50, verbose_name='house address')),
                ('city_of_residence', models.CharField(max_length=40, verbose_name='city')),
                ('local_govt_of_origin', models.CharField(max_length=40, verbose_name='LGA of origin')),
                ('town_or_city_of_origin', models.CharField(max_length=40, verbose_name='town or city')),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="phone number must be entered in the format: '+2340000000000'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='phone number')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]