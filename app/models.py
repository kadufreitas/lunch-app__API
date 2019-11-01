from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=30)
    bank = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='products_photos', null=True, blank=True)
    sellers = models.ManyToManyField(Seller)

    def __str__(self):
        return self.name


class Sale(models.Model):
    value = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    products = models.ManyToManyField(Product ,related_name='list_products')
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
    paid = models.BooleanField(default=False)

    def _update_value_sale(self, created=False):
        if created:
            total_value = 0
            for product in self.products.all():
                total_value += product.value
            Sale.objects.filter(pk=self.pk).update(
                value=total_value)

    def save(self, *args, **kwargs):
        created = self.pk is None
        super(Sale, self).save(*args, **kwargs)
        self._update_value_sale(created)

    def __str__(self):
        return f'Seller: {self.seller} - Client: {self.client} | status: {self.paid}'
