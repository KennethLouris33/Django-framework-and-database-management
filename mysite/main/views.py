from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import CreateNewList
from .models import Item, ToDoList


# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {})

def view(response):
    return render(response, "main/view.html", {})


