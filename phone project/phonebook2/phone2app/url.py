from django.urls import path
from.import views

urlpatterns=[
    path('',views.fun1),
    path('home',views.home,name='home'),
    path('insert',views.insert,name='insert'),
    path('phonebook',views.addphone),
    path('display',views.display,name='display'),
    path('opteration',views.update,name='opteration'),
    # path('update',views.update1,),
    path('update',views.update2),
    path('dlt',views.delete),
    path('home1',views.home2,name='home1'),
    path('home2',views.home2,name='home2'),
    path('home3',views.home2,name='home3'),
    path('home4',views.home2,name='home4'),
    path('about',views.about,name='about'),
        
]

