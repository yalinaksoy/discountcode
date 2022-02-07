# Generated by Django 3.2.11 on 2022-02-07 06:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redeemed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now=True)),
                ('discount_percent', models.FloatField(default=0.1)),
                ('code_string', models.TextField(default=uuid.UUID('8078b80f-2f32-4102-98ac-fc39a832c2d7'))),
                ('brand_id', models.IntegerField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
