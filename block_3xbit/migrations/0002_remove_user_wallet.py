# Generated by Django 2.1.5 on 2019-01-23 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('block_3xbit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='wallet',
        ),
    ]