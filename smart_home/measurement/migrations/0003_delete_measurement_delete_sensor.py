# Generated by Django 4.1.5 on 2023-01-07 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_measurement_image_optional_measurement_updated_at_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Measurement',
        ),
        migrations.DeleteModel(
            name='Sensor',
        ),
    ]