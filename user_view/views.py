from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required , user_passes_test
from appointment.models import Appointment
from .form import CreateUser

#Create User From Owner
@login_required(login_url='login')
@user_passes_test(lambda user: user.is_superuser)
def create_user(request):
    form = CreateUser()
    message = 'Email or username is already exist'
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                newUser = User.objects.create_user(username, email , password)
                newUser.save()
                return redirect('/all_users')
            except:
                return render(request , 'create_user.html' , {'form':form , 'message': message})
        else:
                return render(request , 'create_user.html' , {'form':form , 'message': 'Enter Valid Data'})
    return render(request , 'create_user.html' , {'form':form})


@login_required(login_url='login')
@user_passes_test(lambda user: user.is_superuser)
def user_view(request):
    all_users = User.objects.all()
    users_staff = [x for x in all_users if not x.is_superuser]
    return render(request , 'all_users.html', {'users':users_staff})


@login_required(login_url='login')
@user_passes_test(lambda user: user.is_superuser)
def delete_user(request, id):
    deleted_user = User.objects.get(id=id)
    deleted_user.delete()
    return redirect('/all_users')

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_superuser)
def edit_user(request, id):
    userToUpdate = User.objects.get(id=id)
    if request.method == 'POST':
        userToUpdate.username = request.POST.get('username')
        userToUpdate.mail = request.POST.get('email')
        userToUpdate.password = request.POST.get('password')
        if User.objects.filter(username = userToUpdate.username).exists() == True or User.objects.filter(email = userToUpdate.mail).exists() == True:
                return render(request, 'edit_user.html', {'message' : 'Email or username is already exist'})
        if Appointment.objects.filter(Provider_id = id).exists() == True:
                appointmentUpdate = Appointment.objects.get(Provider_id = id)
                appointmentUpdate.Provider_name = request.POST.get('username')
                appointmentUpdate.save()
        userToUpdate.save()
        return redirect('/all_users')
    else:
        return render(request, 'edit_user.html')
