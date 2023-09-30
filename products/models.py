from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Product(models.Model):
    productType = models.CharField(
        max_length=50, null=False, blank=False, default="")
    productCode = models.IntegerField(default=0)
    productName = models.CharField(
        max_length=150, null=False, blank=False)
    category = models.CharField(
        max_length=50, null=False, blank=False, default="")
    brand = models.CharField(max_length=50, null=False,
                             blank=False, default="")
    unit = models.CharField(max_length=20, null=False, blank=False, default="")
    tax = models.DecimalField(
        max_digits=7, decimal_places=2, null=False, blank=False)
    taxMethod = models.CharField(
        max_length=20, null=False, blank=False, default="")
    image = models.ImageField(
        upload_to='uploads/images', null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    # cate = models.ForeignKey(
    #     Category, on_delete=models.CASCADE, blank=False, null=False)
    # subCate = models.ForeignKey(
    #     SubCategory, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.productName
