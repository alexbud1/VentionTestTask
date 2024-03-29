# Generated by Django 5.0.2 on 2024-02-06 16:36

import django.db.models.deletion
import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=10, max_length=13, prefix='id_', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=10, max_length=13, prefix='id_', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('completed', models.BooleanField(default=False)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.category')),
            ],
            options={
                'ordering': ['completed'],
            },
        ),
    ]
