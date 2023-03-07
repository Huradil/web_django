from django.shortcuts import render,redirect
from django.urls import reverse

from .models import Item,Purchase

def list_item(request):
    items=Item.objects.all()
    context={"items":items,
             }
    return render(request,'list_item.html',context)

def detail_item(request,item_id):
    item=Item.objects.get(id=item_id)
    context={
        "item":item
    }
    return render(request,'detail_item.html',context)





