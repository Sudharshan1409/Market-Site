from django.db import models
from users.models import User

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to="items/images/", blank = True)
    description = models.TextField(blank = True)
    original_cost = models.FloatField()
    revised_cost = models.FloatField()
    stock = models.PositiveIntegerField(default=0)
    sold = models.PositiveIntegerField(default=0)
    booked = models.PositiveIntegerField(default=0)
    category = models.CharField(choices=(('women','Women'),('men','Men'),('childrenboy','Children Boys'),('childrengirl','Children Girls')), max_length=20)
    subcategory = models.CharField(choices=(('saree','Saree'),('kurtis','Kurtis'),('pant','Pant'),('shirt','Shirt'),('other','Other')), max_length=20)
    material_type = models.CharField(choices=(('cotton','Cotton'),('silk','Silk'),('wool','Wool'),('leather','Leather'),('other','Other')), max_length=20)


class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='carts')
    item_quantity = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('user', 'item',)