# Generated by Django 2.2.13 on 2020-09-03 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0031_auto_20200903_0918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name_ph',
            new_name='name_pi',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description_ph',
            new_name='description_pi',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title_ph',
            new_name='title_pi',
        ),
    ]