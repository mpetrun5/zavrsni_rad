# Generated by Django 2.2 on 2019-05-27 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0003_auto_20190527_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='price_excludes',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='price_indcludes',
        ),
        migrations.AlterField(
            model_name='destination',
            name='start_date',
            field=models.DateField(blank=True),
        ),
    ]
