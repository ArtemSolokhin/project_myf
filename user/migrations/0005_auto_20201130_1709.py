# Generated by Django 3.1.3 on 2020-11-30 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20201130_1705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='culture',
            old_name='harvest_time',
            new_name='harvest_days',
        ),
    ]