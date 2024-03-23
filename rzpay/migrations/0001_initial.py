# Generated by Django 3.2.19 on 2023-05-19 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import rzpay.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RazorpayTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('txnid', models.CharField(db_index=True, default=rzpay.models.generate_id, max_length=32)),
                ('basket_id', models.CharField(blank=True, db_index=True, max_length=12, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('currency', models.CharField(blank=True, max_length=8, null=True)),
                ('status', models.CharField(max_length=32)),
                ('rz_id', models.CharField(blank=True, db_index=True, max_length=32, null=True)),
                ('error_code', models.CharField(blank=True, max_length=32, null=True)),
                ('error_message', models.CharField(blank=True, max_length=256, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]
