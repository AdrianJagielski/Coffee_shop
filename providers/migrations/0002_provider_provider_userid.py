# Generated by Django 2.0.7 on 2018-07-25 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='Provider_UserID',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]