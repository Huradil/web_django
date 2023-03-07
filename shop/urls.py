from django.urls import path,include

from . import views

urlpatterns=[
    path('shop/',views.list_item,name='list_item'),
    path('shop/<int:item_id>/',views.detail_item,name='detail_item')
]