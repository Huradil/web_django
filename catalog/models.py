from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ProductModel(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    sold=models.BooleanField()
    date=models.DateField()

    def __str__(self):
        return f'{self.name} - {self.category}'

