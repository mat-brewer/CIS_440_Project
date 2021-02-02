from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Success! Account Created.")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {"form":form})

# the reason it is not saving is because the password is too common