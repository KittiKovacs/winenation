# Generated by Django 3.1.6 on 2021-03-12 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20210311_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
