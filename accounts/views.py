from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import CustomUserForm
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = CustomUserForm()
    return render(request, "accounts/signup.html")
