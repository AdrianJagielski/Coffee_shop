# Generated by Django 2.0.7 on 2018-07-25 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0006_auto_20180725_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='Provider_UserID',
            field=models.IntegerField(null=True),
        ),
    ]
