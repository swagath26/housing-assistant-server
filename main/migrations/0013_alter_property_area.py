# Generated by Django 5.0 on 2024-02-03 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_property_address_alter_property_balcony_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='area',
            field=models.CharField(blank=True, null=True),
        ),
    ]
