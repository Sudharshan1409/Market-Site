# Generated by Django 3.0.7 on 2020-06-29 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('image', models.ImageField(blank=True, upload_to='items/images/')),
                ('description', models.TextField(blank=True)),
                ('original_cost', models.FloatField()),
                ('revised_cost', models.FloatField()),
                ('stock', models.PositiveIntegerField(default=0)),
                ('sold', models.PositiveIntegerField(default=0)),
                ('booked', models.PositiveIntegerField(default=0)),
                ('category', models.CharField(choices=[('women', 'Women'), ('men', 'Men'), ('childrenboy', 'Children Boys'), ('childrengirl', 'Children Girls')], max_length=20)),
                ('subcategory', models.CharField(choices=[('saree', 'Saree'), ('kurtis', 'Kurtis'), ('pant', 'Pant'), ('shirt', 'Shirt'), ('other', 'Other')], max_length=20)),
                ('material_type', models.CharField(choices=[('cotton', 'Cotton'), ('silk', 'Silk'), ('wool', 'Wool'), ('leather', 'Leather'), ('other', 'Other')], max_length=20)),
            ],
        ),
    ]
