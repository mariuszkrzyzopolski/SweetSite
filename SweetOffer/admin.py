from django.contrib import admin

from .models import Offer, Ingredient, Description, Image, IngredientOffer


class IngredientInline(admin.TabularInline):
    model = IngredientOffer
    extra = 1


class DescriptionInline(admin.TabularInline):
    model = Description
    extra = 1


class ImageInline(admin.TabularInline):
    model = Image


class OfferAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'offer_text']}),
        ('Data publikacji', {'fields': ['pub_date']}),
    ]
    inlines = [IngredientInline, DescriptionInline, ImageInline]


admin.site.register(Offer, OfferAdmin)
admin.site.register(Ingredient)
