# Generated by Django 3.1.6 on 2021-02-21 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210216_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='alc_vol',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='pairing',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='vintage',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
