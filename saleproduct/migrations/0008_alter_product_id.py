# Generated by Django 4.1.7 on 2023-02-16 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saleproduct', '0007_alter_productimage_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]