# Generated by Django 3.0.7 on 2020-07-01 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_auto_20200701_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='newly_arrived',
            field=models.BooleanField(default=True),
        ),
    ]
