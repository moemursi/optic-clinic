# Generated by Django 2.0.1 on 2018-01-22 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_prescription_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescription',
            old_name='Photochromic',
            new_name='photochromic',
        ),
        migrations.AlterField(
            model_name='prescription',
            name='doctor',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinic.Doctor'),
        ),
    ]