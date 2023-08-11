from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    Provider_id = models.ForeignKey(User , on_delete=models.SET_NULL, null=True)
    Provider_name = models.CharField(max_length=100)
    Emarat = models.CharField(max_length=50)
    Location = models.CharField(max_length=100)
    Guest = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Note = models.TextField(max_length=500, blank=True)
    Date = models.DateField()
    Time = models.TimeField(auto_now=False)
    phone = models.CharField(max_length=11)

    def __str__(self) -> str:
        return self.Email
    
    class Meta:
        constraints  = [
            models.UniqueConstraint(fields=['Date', 'Time'], name='Date and Time')]