# Generated by Django 2.2.14 on 2021-05-14 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='disable',
            field=models.BooleanField(default=False),
        ),
    ]
