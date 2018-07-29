# Generated by Django 2.0.7 on 2018-07-29 20:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0005_auto_20180729_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='Offer_Realization_Time',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator(message='Atleast 1 and less than 3 digits', regex='^[0-9]{1,3}$')]),
        ),
    ]
