# Generated by Django 2.0.7 on 2018-07-25 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0002_provider_provider_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='Provider_UserID',
            field=models.IntegerField(null=True),
        ),
    ]
