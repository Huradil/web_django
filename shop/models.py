from django.db import models

class Item(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.price}'

class Purchase(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    item=models.ForeignKey(Item,on_delete=models.CASCADE,related_name='purchases')

    def __str__(self):
        return f'{self.name} {self.item}'
