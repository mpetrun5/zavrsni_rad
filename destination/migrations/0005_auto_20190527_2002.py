# Generated by Django 2.2 on 2019-05-27 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0004_auto_20190527_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
