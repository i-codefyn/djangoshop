# Generated by Django 2.2.13 on 2020-07-24 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0018_auto_20200723_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='top_seller',
            field=models.BooleanField(default=True),
        ),
    ]
