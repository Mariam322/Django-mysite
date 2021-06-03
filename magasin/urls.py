from django.urls import path,include
from .import views
urlpatterns=[
    path('',views.index1),
     path('listproduit/',views.index),
    path('majProduits/',views.index2),
    path('cart/', views.cart, name="cart"),
    path('checkup/',views.checkup,name="checkup"),
    path('mesCommandes/', views.mesCommandes, name='mesCommandes'),
    

    ]