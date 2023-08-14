from django.shortcuts import render , HttpResponse
from .models import Item
# Create your views here.
def index(request):
    
    return render(request ,'item/base.html')

def about(request):
    product = Item.objects.all()
    
    return render(request, 'item/index.html' , {'product':product})

def shoping(request , pk):
    product  = Item.objects.filter(name=pk)
    
    
    return render(request , 'item/shoping.html',{'product':product})