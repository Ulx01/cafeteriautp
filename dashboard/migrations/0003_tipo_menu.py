# Generated by Django 2.0.6 on 2018-07-10 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_meal_tipo_meal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_economico', models.FloatField()),
                ('menu_normal', models.FloatField()),
                ('menu_jumbo', models.FloatField()),
            ],
        ),
    ]
