# Generated by Django 3.0.7 on 2020-06-30 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_item_newly_arrived'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='subcategory',
            field=models.CharField(choices=[('saree', 'Saree'), ('kurtis', 'Kurtis'), ('pant', 'Pant'), ('shirt', 'Shirt'), ('top', 'Top'), ('jeans', 'Jeans'), ('chudidhar', 'Chididhar'), ('other', 'Other')], max_length=20),
        ),
    ]
