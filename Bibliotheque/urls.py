from django.urls import path,include
from .import views
urlpatterns=[
    path('',views.index7),
    path('livres/', views.livres, name="livres"),
    path('contact/', views.contact, name="contact"),
    path('cont/', views.cont, name="cont"),

    ]