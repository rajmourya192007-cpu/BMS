from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return self.name
