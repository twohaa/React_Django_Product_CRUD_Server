# Generated by Django 4.2.3 on 2023-08-02 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category_subcategory_product_cate_product_subcate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subCate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.subcategory'),
        ),
    ]
