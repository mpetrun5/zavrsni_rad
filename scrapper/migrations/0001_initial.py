# Generated by Django 2.2 on 2019-04-13 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Selector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offers_url', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('travel_plan', models.CharField(blank=True, max_length=100)),
                ('price_includes', models.CharField(blank=True, max_length=100)),
                ('price_excludes', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('image_gallery', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
