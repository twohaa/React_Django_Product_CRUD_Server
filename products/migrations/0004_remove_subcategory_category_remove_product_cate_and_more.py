# Generated by Django 4.2.3 on 2023-08-02 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_cate_alter_product_subcate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='cate',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subCate',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
