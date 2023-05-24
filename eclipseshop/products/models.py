from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name', ]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    # category on_delete=PROTECT means you can't delete category filled with products
    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT)
    name = models.CharField(max_length=300, db_index=True)
    multiple_types_helper = models.CharField(max_length=100, blank=True, null=True)
    tech_specs = models.ManyToManyField('TechSpec', related_name='tech_specs', blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    short_desc = models.TextField(max_length=270, blank=True, null=True)
    full_desc = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    carousel_2_img = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    carousel_3_img = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category', 'name', ]
        index_together = (('id', 'slug'), )

    def __str__(self):
        return f'{self.name} in {self.category}'


class TechSpec(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    product_helper = models.ManyToManyField('Category', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.description}), products: {", ".join(str(prod) for prod in self.product_helper.all())}'
