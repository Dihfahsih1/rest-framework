# Generated by Django 4.1.1 on 2022-09-10 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(default='Title Nmae', max_length=120),
            preserve_default=False,
        ),
    ]