# Generated by Django 2.0.6 on 2018-07-10 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_tipo_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='quantity_meal',
            field=models.IntegerField(default=0),
        ),
    ]
