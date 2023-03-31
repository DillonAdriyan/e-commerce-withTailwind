# Generated by Django 4.1.7 on 2023-03-31 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saleproduct', '0022_rename_variantimage_productvariants_variant_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ('name',), 'verbose_name': 'Phân loại', 'verbose_name_plural': 'Phân loại'},
        ),
        migrations.AlterField(
            model_name='productvariants',
            name='variant_image',
            field=models.ImageField(blank=True, null=True, upload_to='res/image/variants', verbose_name='Ảnh sản phẩm'),
        ),
    ]
