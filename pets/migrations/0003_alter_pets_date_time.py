# Generated by Django 4.0.4 on 2022-08-20 04:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_alter_pets_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pets',
            name='date_time',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]