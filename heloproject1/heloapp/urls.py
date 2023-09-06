from .import views
from django.urls import path

urlpatterns = [

    path('',views.operations, name='operations'),
   # path('calculate/',views.calculate,name='calculate'),

]
