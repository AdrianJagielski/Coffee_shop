# Generated by Django 2.0.7 on 2018-07-28 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0012_auto_20180729_0129'),
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='Offer_Name',
        ),
        migrations.AddField(
            model_name='offer',
            name='provider_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='providers.Provider'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='offer',
            name='Offer_Contact',
            field=models.TextField(max_length=68),
        ),
        migrations.AlterField(
            model_name='offer',
            name='Offer_Ware',
            field=models.TextField(max_length=68),
        ),
    ]
