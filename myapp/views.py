from django.shortcuts import render,HttpResponse


def main(request) :
   return render(request , 'item/main.html')
