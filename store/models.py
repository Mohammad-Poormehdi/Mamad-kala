from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    price = models.PositiveBigIntegerField()
    image = models.ImageField(blank=True,null=True, upload_to='files/')
    
    def __str__(self):
        return self.name