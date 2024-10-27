from django.shortcuts import render

# Create your views here.
def busInfo(request):
    d={'routes':[{'id':'bus1','area':'dharmavaram'},
                 {'id':'bus2','area':'atp'},
                 {'id':'bus3','area':'tadipatri'},
                 {'id':'bus4','area':'pamidi'},
                 {'id':'bus5','area':'Bks'}]}
    return render(request,'info.html',d)