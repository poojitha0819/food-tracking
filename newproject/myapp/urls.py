from django.urls import path
from .import views

urlpatterns=[
    path('',views.loadLogin),
    path('loadfood',views.loadFood,name='loadfood'),
    path('index',views.Index,name='Index'),
    path('addFood',views.addFood,name='addfood'),
    path('userlogin',views.userlogin),
    path('del/<int:fid>',views.delFood,name='delFood')

]