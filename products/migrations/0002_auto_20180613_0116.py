# Generated by Django 2.0.1 on 2018-06-12 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariant',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]