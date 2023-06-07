from django.db import models
from base.models import User

# Create your models here.

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta: 
        verbose_name_plural = "Chat"        
    def __str__(self): 
        return f'{self.user.username} : {self.message}'
    
    
