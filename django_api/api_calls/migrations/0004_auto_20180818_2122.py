# Generated by Django 2.1 on 2018-08-18 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_calls', '0003_service_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='service_provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.TextField()),
                ('sa_name', models.TextField()),
                ('cost', models.FloatField()),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='service_area',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='service_area',
            name='lng',
        ),
        migrations.RemoveField(
            model_name='service_area',
            name='name',
        ),
    ]
