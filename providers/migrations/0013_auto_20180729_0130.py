# Generated by Django 2.0.7 on 2018-07-28 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0012_auto_20180729_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='provider',
            name='Provider_name',
            field=models.CharField(max_length=200),
        ),
    ]