# Generated by Django 2.2 on 2019-05-27 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0009_remove_destination_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]