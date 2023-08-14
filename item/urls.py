from django.urls import path
from .views import index ,  about , shoping

app_name = 'item'

urlpatterns = [

     path('' , index , name='index') ,
     path('product/' ,about , name='about' ),
     path('product/<str:pk>' , shoping , name='shoping' )
]
