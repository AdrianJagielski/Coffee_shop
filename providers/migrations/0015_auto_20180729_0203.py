# Generated by Django 2.0.7 on 2018-07-29 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0014_auto_20180729_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='Provider_name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, unique=True),
        ),
    ]
