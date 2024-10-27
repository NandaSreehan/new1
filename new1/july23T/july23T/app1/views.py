from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def func1(request):
    d={
        'place':'vizag'
    }
    return render(request,'home.html',d)





def func2(request):
    d1={'name':'appalaraju','age':18,'status':'Eligible'}
    return render(request,'vote.html',d1)




def func3(request):
    d2={'movies':[
        {'name':'varsham','year':2004,'director':'Naveen'},
        {'name':'Salaar','year':2024,'director':'Prashanth Neelu'},
        {'name':'Billa','year':2008,'director':'yeshwanth'}
        ]}
    return render(request,'movies.html',d2)