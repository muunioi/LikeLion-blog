# Generated by Django 3.0.7 on 2020-06-04 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='Blog',
        ),
    ]