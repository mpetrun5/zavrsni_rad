# Generated by Django 2.2 on 2019-05-27 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0011_auto_20190527_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]