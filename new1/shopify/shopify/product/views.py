from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def msearch(request,pid):
    mobiles=[{'id':1,'name':"Iqoo Neo 7 Pro",'config':['12gb','256gb'],'cost':36000},
             {'id':2,'name':'Redmi 13 pro','config':['8gb','128gb'],'cost':10},
             {'id':3,'name':'Nokia S','config':['8gb','64gb'],'cost':20},
             {'id':4,'name':'iPhone','config':['0gb','512gb'],'cost':0.50}]
    result=None
    for item in mobiles:
        if item.get('id')==pid:
            result=item
            break
    if result is not None:
        return HttpResponse(f"<p>Mobile Name: {result.get('name')}<br>Cost: {result.get('cost')} <br>Configuration: {result.get('config')}</p>")
    else:
        return HttpResponse("Sorry Dude NO result matched")
def lsearch(request,pid):
    laptops=[
    {'id':1,'name':"HP",'config':['16gb','1TB'],'cost':70000},
    {'id':2,'name':'Lenovo','config':['8gb','512gb'],'cost':10000},
    {'id':3,'name':'Dell','config':['32gb','1TB'],'cost':100000},
    {'id':4,'name':'MacBook','config':['0gb','512gb'],'cost':50}]
    result=None
    for item in laptops:
        if item.get('id')==pid:
            result=item
            break
    if result is not None:
        return HttpResponse(f"<p>Laptop Name: {result.get('name')}<br>Cost: {result.get('cost')} <br>Configuration: {result.get('config')}</p>")
    else:
        return HttpResponse("Sorry Dude NO result matched")
    #return HttpResponse()

def asearch(request,pid):
    airpods=[
    {'id':1,'name':"Airpods Pro gen1",'cost':26000},
    {'id':2,'name':'TWS','cost':10000},
    {'id':3,'name':'Noise','cost':100},
    {'id':4,'name':'onePlus','cost':10}]
    result=None
    for item in airpods:
        if item.get('id')==pid:
            result=item
            break
    if result is not None:
        return HttpResponse(f"<p>Brand Name: {result.get('name')}<br>Cost: {result.get('cost')}</p>")
    else:
        return HttpResponse("Sorry Dude NO result matched")

    #return HttpResponse()