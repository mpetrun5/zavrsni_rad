# Generated by Django 2.2 on 2019-04-13 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('original_url', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('price_indcludes', models.TextField()),
                ('price_excludes', models.TextField()),
                ('num_of_nights', models.PositiveIntegerField()),
                ('is_active', models.BooleanField()),
                ('start_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='destination.Country')),
            ],
        ),
        migrations.CreateModel(
            name='DailyOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='destination.Destination')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='destination.Location')),
            ],
        ),
    ]