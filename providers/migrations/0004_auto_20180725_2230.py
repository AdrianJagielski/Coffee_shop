# Generated by Django 2.0.7 on 2018-07-25 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0003_auto_20180725_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='Provider_UserID',
            field=models.IntegerField(default=0),
        ),
    ]