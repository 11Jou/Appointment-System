from django.shortcuts import render
from .models import Appointment
from django.contrib.auth.decorators import login_required , user_passes_test
from itertools import groupby
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.mail import send_mail
import yagmail
from django.conf import settings

months = {"January":'01', "February":'02', "March":'03', "April":'04', "May":'05', "June":'06', "July":'07', "August":'08', "September":'9'
            , "October":'10', "November":'11', "December":'12'}

@login_required(login_url='login')
def calender_view(request):
    return render(request, 'schedule.html')


@login_required(login_url='login')
def appointment_details(request):
    current_user = request.user
    provider_user = User.objects.get(id=current_user.id)
    day = request.GET.get('date')
    time = request.GET.get('time')
    month = request.GET.get('month')
    date = '2023-{}-{}'.format(months[month],day)
    if request.method == "POST":
        emarat = request.POST.get('country')
        location = request.POST.get('location')
        guest = request.POST.get('Episode_guest')
        email = request.POST.get('mail')
        phone = request.POST.get('phone')
        note = request.POST.get('notes')
        appointment = Appointment(Provider_id = provider_user, Provider_name = provider_user.username , 
                                Emarat = emarat , Location = location
                                , Guest = guest, Email = email, Note = note, Date=date, Time=time)
        appointment.save()
        send_email(request, guest, date, time, emarat, location, note, email ,phone)
        return render(request, 'details_booking.html', {'date': day,'time': time,'month': month, 'message':'Appointment is submitted'})
    return render(request, 'details_booking.html', {'date': day,'time': time,'month': month,})


def send_email(request, guest, date, time, emarat, location, note, customer_email,phone):
    subject = 'Interview Details'
    html_content = render_to_string('email.html', context={'guest':guest , 'date':date, 'time':time, 
                                                'emarat':emarat, 'location':location,
                                                "customer":customer_email, 'phone':phone})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject , text_content, settings.EMAIL_HOST_USER ,[customer_email] )
    email.attach_alternative(html_content , "text/html")
    email.send()

def check_appointment_exists(request):
    day = request.GET.get('date')
    time = "{}:00".format(request.GET.get('time'))
    month = request.GET.get('month')
    date = '2023-{}-{}'.format(months[month],day)
    appointment_exists = Appointment.objects.filter(Date=date, Time=time).exists()
    return JsonResponse({'exists': appointment_exists})



@login_required(login_url='login')
def view_user_booking(request, id):
    if request.user.is_superuser or request.user.id == id:
        data = Appointment.objects.filter(Provider_id=id)
        return render(request, 'all_booking.html', {'data':data} )
    else:
        raise PermissionError
    

def view_appointment_details(request , id):
    data = Appointment.objects.filter(id=id)
    return render(request , 'all_booking.html', {'data' : data})



@login_required(login_url='login')
@user_passes_test(lambda user: user.is_superuser)
def view_all_booking(request):
    appointments = Appointment.objects.all().order_by('Date')
    data = {}
    for date, group in groupby(appointments, key=lambda x: x.Date):
            data[date] = list(group)
    return render(request , 'appointment.html', {'data':data})