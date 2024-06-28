from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm

# Create your views here.

def registration(request):
    if request.method == 'POST': # Checking if the user is clicking signup button
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Login successful, Welcome {username}')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/user-registration.html', {'form':form})

@login_required
def profile_page(request):
    return render(request, 'users/profile.html')
