# Generated by Django 4.1.7 on 2023-03-16 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0008_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_name',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
