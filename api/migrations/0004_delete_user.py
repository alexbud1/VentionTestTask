# Generated by Django 5.0.2 on 2024-02-06 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
