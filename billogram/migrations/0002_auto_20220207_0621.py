# Generated by Django 3.2.11 on 2022-02-07 06:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('billogram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountcode',
            name='code_string',
            field=models.TextField(default=uuid.UUID('c1851b1f-2626-49cf-881a-29f65ad4da4e')),
        ),
        migrations.AlterField(
            model_name='discountcode',
            name='discount_percent',
            field=models.DecimalField(decimal_places=3, default=0.1, max_digits=5),
        ),
    ]
