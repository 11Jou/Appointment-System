
from django.contrib import admin
from django.urls import path , include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name='index'),
    path('', include('login.urls')),
    path('', include('user_view.urls')),
    path('', include('appointment.urls')),


]
