# Generated by Django 2.0.7 on 2018-07-29 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0006_auto_20180729_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='Offer_Products',
            field=models.TextField(max_length=200),
        ),
    ]
