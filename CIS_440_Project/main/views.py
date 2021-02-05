from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def main(request):
    '''function to display the apps home page'''

    # checks if user is authenticated
    #if request.user.is_authenticated:
    #    return redirect("/dashboard/")
    #else:
    # essenitally will render the given html page and make that the "view" for main
    return render(request, 'main/index.html')

def menu(request):
    return render(request, 'main/menu.html')

def about(request):
    return render(request, 'main/about.html')

def order(request):
    return render(request, 'main/order.html')

def reviews(request):
    return render(request, 'main/reviews.html')