# Generated by Django 3.2.11 on 2022-01-15 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220115_0901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survivor',
            name='infection_flag',
        ),
    ]
