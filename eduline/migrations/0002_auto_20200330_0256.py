# Generated by Django 2.2.7 on 2020-03-30 01:56

from django.db import migrations, models

import eduline.models


class Migration(migrations.Migration):
    dependencies = [
        ('eduline', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='book.gif', upload_to=eduline.models.get_upload_path),
        ),
    ]