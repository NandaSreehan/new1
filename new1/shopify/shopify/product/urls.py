from django.urls import path
from product import views

urlpatterns=[
    path('mobiles/<int:pid>',views.msearch,name="ms"),
    path('laptops/<int:pid>',views.lsearch,name="ls"),
    path('airpods/<int:pid>',views.asearch,name="as"),
    
]