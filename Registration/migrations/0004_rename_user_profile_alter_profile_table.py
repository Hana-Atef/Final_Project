# Generated by Django 4.1.7 on 2023-03-13 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0003_alter_user_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Profile',
        ),
        migrations.AlterModelTable(
            name='profile',
            table='Profile',
        ),
    ]
