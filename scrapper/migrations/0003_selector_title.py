# Generated by Django 2.2 on 2019-04-13 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0002_selector_agency'),
    ]

    operations = [
        migrations.AddField(
            model_name='selector',
            name='title',
            field=models.CharField(default='Atena', max_length=100),
            preserve_default=False,
        ),
    ]
