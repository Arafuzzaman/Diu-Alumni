# Generated by Django 4.1.2 on 2022-12-30 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_gallery'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='image',
            new_name='img',
        ),
    ]
