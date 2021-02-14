from django.shortcuts import render
from django.contrib import messages
from django.views.generic import (
    ListView, 
    TemplateView, 
    DetailView,
    CreateView, 
    UpdateView, 
    DeleteView)
from .models import MenuItem
from orders import models as orders

# Create your views here.
def main(request):
    '''function to display the apps home page'''

    # checks if user is authenticated
    #if request.user.is_authenticated:
    #    return redirect("/dashboard/")
    #else:
    # essenitally will render the given html page and make that the "view" for main
    return render(request, 'main/index.html')

class MenuListView(ListView):
    template_name = 'main/menu.html'
    model = MenuItem
    context_object_name = "items"


def about(request):
    return render(request, 'main/about.html')

def login(request):
    return render(request, 'users/login.html')