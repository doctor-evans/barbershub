# Generated by Django 3.1.3 on 2020-11-20 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbers', '0005_gallery_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
