from shop.models import Item,Purchase

item1=Item.objects.create(name="milk",price=50)
item2=Item.objects.create(name="bread",price=20)
item3=Item.objects.create(name="butter",price=100)
item4=Item.objects.create(name="sugar",price=40)
item5=Item.objects.create(name="solt",price=8)
purchase1=Purchase.objects.create(name="Nuradil",age=19,item=item1)
purchase2=Purchase.objects.create(name="Asanbek",age=19,item=item2)
purchase3=Purchase.objects.create(name="Nurlan",age=29,item=item3)
purchase4=Purchase.objects.create(name="Kasiet",age=12,item=item4)
purchase5=Purchase.objects.create(name="Alexsandr",age=20,item=item5)
items=Item.objects.all()
purchases=Purchase.objects.all()
items
purchases
