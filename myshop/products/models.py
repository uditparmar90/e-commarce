from django.db import models

# Create your models here.

class Address(models.Model):
    street=models.CharField(max_length=50)
    zipcode=models.PositiveIntegerField()
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.city}-{self.country}"

class Brand(models.Model):
    title = models.CharField(max_length= 70)
    logo = models.ImageField()
    address=models.OneToOneField(Address,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title}"


class Shirt(models.Model):
    title = models.CharField(max_length= 70)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    is_bestseller = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"


class Category(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField( max_length=50, null=True)
    def __str__(self):
        return f"{self.title}"

class Product(models.Model):
    title = models.CharField(max_length= 70)
    description = models.TextField()
    # many to many relationship
    cat = models.ManyToManyField(Category)
    image = models.ImageField(blank= True, upload_to='product-img')
    # one to one ralationship
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField()
    slug = models.SlugField(blank=True)
    is_bestseller = models.BooleanField(default=False)
    # -------------manay to manny ralationship within model------------ex-product suggestion within a particular roduct
    suggestion=models.ManyToManyField('self')

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = self.id
        super().save(*args, **kwargs)



