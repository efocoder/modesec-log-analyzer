# Generated by Django 4.1.7 on 2023-03-06 21:38

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0008_alter_analysis_log_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='description',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None),
        ),
    ]
