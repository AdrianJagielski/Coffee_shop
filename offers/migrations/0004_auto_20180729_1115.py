# Generated by Django 2.0.7 on 2018-07-29 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0003_auto_20180729_0158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='Offer_NIP',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='Offer_Phone',
        ),
    ]
