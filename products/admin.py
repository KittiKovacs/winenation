from django.contrib import admin
from .models import (Product, Category, Variety,
                     Wine_region, Event, Subscription)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class VarietyAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class Wine_regionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'winery',
        'variety',
        'vintage',
        'region',
        'description',
        'alc_vol',
        'pairing',
        'price',
        'image',
    )

    ordering = ('sku',)


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
        'price',
        'image',
    )


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
        'price',
        'image',
    )


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Variety, VarietyAdmin)
admin.site.register(Wine_region, Wine_regionAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
