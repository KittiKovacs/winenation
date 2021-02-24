from django.contrib import admin
from .models import (Wine, Category, Variety,
                     Wine_region, Subscription)


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


class WineAdmin(admin.ModelAdmin):
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


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
        'price',
        'image',
    )


# Register your models here.
admin.site.register(Wine, WineAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Variety, VarietyAdmin)
admin.site.register(Wine_region, Wine_regionAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
