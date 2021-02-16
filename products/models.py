from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Variety(models.Model):

    class Meta:
        verbose_name_plural = 'Varieties'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Wine_region(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    class Meta:
        abstract = True

    sku = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Wine(Product):
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    winery = models.CharField(max_length=254)
    variety = models.ForeignKey('Variety', null=True, blank=True,
                                on_delete=models.SET_NULL, max_length=254)
    vintage = models.IntegerField()
    region = models.ForeignKey('Wine_region', null=True, blank=True,
                               on_delete=models.SET_NULL, max_length=254)
    alc_vol = models.DecimalField(max_digits=6, decimal_places=2)
    pairing = models.CharField(max_length=254)


class Event(Product):
    sku = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)


class Subscription(Product):
    sku = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
