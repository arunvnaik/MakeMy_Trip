# Generated by Django 5.0.3 on 2024-03-05 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_app', '0002_alter_customer_age_alter_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cost',
            name='price',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=10, unique=True),
        ),
    ]
