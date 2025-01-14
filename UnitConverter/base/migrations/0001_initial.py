# Generated by Django 5.1 on 2024-09-26 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_unit', models.CharField(max_length=20)),
                ('to_unit', models.CharField(max_length=20)),
                ('value', models.FloatField()),
                ('converted_value', models.FloatField()),
            ],
        ),
    ]
