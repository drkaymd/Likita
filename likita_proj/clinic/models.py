from django.db import models
from base.models import User
from datetime import datetime

# Create your models here.

SERVICE_CHOICES = (
    ("Condultation", "Consultation"),
    ("Nursing care", "Nursing care"),
    ("Medical social services", "Medical social services"),
    ("Counselling", "Counselling"),
    ("Homemaker or basic assistance care", "Homemaker or basic assistance care"),
    )
TIME_CHOICES = (
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
)

class Appointment(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField()
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="Consultation")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    phone = models.CharField(max_length=20)
    message = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name_plural = 'Appointment'
        ordering = ['-updated_at', '-created_at']
        
    def __str__(self):
        return f"{self.name.username} | day: {self.day} | time: {self.time}"


