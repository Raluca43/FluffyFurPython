# Generated by Django 4.0.4 on 2022-06-04 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pets',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]