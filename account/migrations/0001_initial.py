# Generated by Django 4.1.2 on 2022-11-12 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('varsityEmail', models.EmailField(blank=True, max_length=50, null=True)),
                ('varsityId', models.CharField(blank=True, default=False, max_length=25, null=True)),
                ('linkedIn', models.CharField(blank=True, default=False, max_length=500, null=True)),
                ('password1', models.CharField(max_length=20, null=True)),
                ('password2', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
