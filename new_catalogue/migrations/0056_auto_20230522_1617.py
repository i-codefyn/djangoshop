# Generated by Django 2.2.13 on 2023-05-22 10:47

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0055_auto_20200921_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name_ar',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_fi',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description_ar',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description_fi',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title_ar',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title_fi',
        ),
        migrations.AlterField(
            model_name='product',
            name='colour',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('RED', 'Red'), ('BLU', 'Blue'), ('GRN', 'Green'), ('WH', 'White'), ('PNK', 'Pink'), ('YLW', 'Yellow')], default='', max_length=22),
        ),
    ]
