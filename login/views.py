from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required , user_passes_test
from django.shortcuts import render, redirect
from .form import LoginForm


#Login for owner and employee
def login_view(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/all_users')
        else:
            return redirect("schedule/calender")
    form = LoginForm()
    message = 'username or password is incorrect'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username , password = password)
            if user:
                login(request, user)
                return redirect("/")
            else:
                return render(request, 'login.html' , {'form':form, 'error_message': message})
        else:
                return render(request , 'login.html' , {'form':form , 'error_message': 'Enter Valid Data'})

    return render(request, 'login.html', {'form': form})


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('/')
