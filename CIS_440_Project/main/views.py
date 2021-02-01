from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def main(request):
    '''function to display the apps home page'''

    # makes dashboard the home page for logged in users
    #if request.user.is_authenticated:
    #    return redirect("/dashboard/")
    #else:
    return render(request, 'main/index.html')