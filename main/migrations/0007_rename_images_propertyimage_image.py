# Generated by Django 5.0 on 2024-01-20 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_image_propertyimage_images_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertyimage',
            old_name='images',
            new_name='image',
        ),
    ]
