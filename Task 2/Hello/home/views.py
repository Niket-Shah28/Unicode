from django.http import HttpResponse
from django.shortcuts import render
from home import task1

# Create your views here.
def index(request,n1,n2):
      output=task1.binary(n1,n2)
      return HttpResponse("<h1>The dictionary is %s</h1>" %output)




