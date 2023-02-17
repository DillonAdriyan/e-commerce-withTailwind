# Generated by Django 4.1.7 on 2023-02-17 00:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('saleproduct', '0011_homebannercontent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimage',
            options={'ordering': ('date_created',), 'verbose_name': 'product image', 'verbose_name_plural': 'product images'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='is_main',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='saleproduct.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productimage',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='productimage',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='saleproduct.product')),
            ],
            options={
                'verbose_name': 'product attribute',
                'verbose_name_plural': 'product attributes',
                'ordering': ('name',),
            },
        ),
    ]
