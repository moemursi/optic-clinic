# Generated by Django 2.0.1 on 2018-01-22 00:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('other_name', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=7)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('other_name', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=7)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('occupation', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left_sph', models.CharField(blank=True, max_length=6, null=True)),
                ('left_cyl', models.CharField(blank=True, max_length=6, null=True)),
                ('left_axis', models.CharField(blank=True, max_length=6, null=True)),
                ('left_add', models.CharField(blank=True, max_length=6, null=True)),
                ('right_sph', models.CharField(blank=True, max_length=6, null=True)),
                ('right_cyl', models.CharField(blank=True, max_length=6, null=True)),
                ('right_axis', models.CharField(blank=True, max_length=6, null=True)),
                ('right_add', models.CharField(blank=True, max_length=6, null=True)),
                ('Photochromic', models.BooleanField(default=False)),
                ('comment', models.TextField(blank=True, max_length=100, null=True)),
                ('no_prescription', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinic.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.Patient')),
            ],
        ),
    ]
