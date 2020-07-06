import math

from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField(default=0)

    class Meta:
        ordering = ['name',]

    def __str__(self):
        return self.name


class Type(models.Model):
    type_name = models.CharField(max_length=100)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.type_name


class Offer(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    type_offer = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def sum_price(self):
        all_ingredients = IngredientOffer.objects.filter(offer=self)
        price = 0
        for i in all_ingredients:
            price += i.count * i.ingredient.price
        return round(price, 0)


class IngredientOffer(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    count = models.FloatField(default=1)


class Image(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    image_link = models.CharField(max_length=300)


class Description(models.Model):
    description_text = models.CharField(max_length=300)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

    def __str__(self):
        return self.description_text
