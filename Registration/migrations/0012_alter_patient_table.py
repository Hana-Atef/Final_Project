# Generated by Django 4.1.7 on 2023-04-02 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0011_alter_patient_dob_alter_patient_patient_name'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='patient',
            table='Patient',
        ),
    ]
