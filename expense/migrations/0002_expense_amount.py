# Generated by Django 2.2.4 on 2019-08-24 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='amount',
            field=models.FloatField(default=0, max_length=6),
        ),
    ]
