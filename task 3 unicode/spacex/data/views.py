from django.shortcuts import render,HttpResponse
from .forms import InfoForm
import requests

# Create your views here.
def index(request):
    response=requests.get("https://api.spacexdata.com/v3/launches/next").json()
    if request.method == "POST":
        fn=InfoForm(request.POST)
        if fn.is_valid():
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
        fn=InfoForm()
        return render(request,'form.html',{'form':fn})


