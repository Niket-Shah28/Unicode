from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('<int:n1>/<int:n2>',views.index,name='home')
]
