# Generated by Django 4.1.2 on 2022-12-30 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='media')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
        ),
    ]
