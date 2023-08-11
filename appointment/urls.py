from django.urls import path
from . import views

urlpatterns = [
    path('schedule' , views.calender_view , name='calender'),
    path('details_booking/' , views.appointment_details , name='details'),
    path('user_booking/<int:id>' , views.view_user_booking , name='user_booking'),
    path('all_booking', views.view_all_booking , name='all_booking'),
    path('one_booking/<int:id>', views.view_appointment_details , name='one_booking'),
    path('check_appointment/', views.check_appointment_exists, name='check_appointment'),
]