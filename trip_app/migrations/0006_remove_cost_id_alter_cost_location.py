# Generated by Django 5.0.3 on 2024-03-05 06:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_app', '0005_alter_cost_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cost',
            name='id',
        ),
        migrations.AlterField(
            model_name='cost',
            name='location',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='trip_app.location'),
        ),
    ]
