from django.contrib import admin
from .models import (Product, Category, Variety,
                     Wine_region, Events, Subscriptions)


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


class EventsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
        'date',
        'price',
        'image',
    )


class SubscriptionsAdmin(admin.ModelAdmin):
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
admin.site.register(Events, EventsAdmin)
admin.site.register(Subscriptions, SubscriptionsAdmin)
