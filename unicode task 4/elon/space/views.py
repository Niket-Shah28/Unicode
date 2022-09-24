from django.shortcuts import render,HttpResponse
import requests
from .forms import Data
from .models import SpaceX

# Create your views here.
def index(request):
    response=requests.get("https://api.spacexdata.com/v3/launches/next").json()
    if request.method == "POST":
        fn=Data(request.POST)
        if fn.is_valid():
            fn.save()
            if fn.cleaned_data['Field']==("details"):
                rep=response["details"]
            if fn.cleaned_data['Field']==("links"):
                rep=response["links"]
            if fn.cleaned_data['Field']==("mission_name"):
                rep=response["mission_name"]  
            if fn.cleaned_data['Field']==("rocket"):
                rep=response["rocket"]
        return render(request,'print.html',{'rep':rep})
    else:
        fn=Data()
        Info=SpaceX.objects.all()
        return render(request,'form.html',{'form':fn,'stu':Info})


