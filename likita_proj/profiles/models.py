from django.db import models
import uuid
from datetime import datetime

# Create your models here.

class ContactUs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())
    
    class  Meta:
        verbose_name_plural = 'ContactUs'
        ordering = ['-created_at']
        
    def __str__(self):
        return f'{self.email} : {self.message[:30]}'
    
    
    
    
class ReplyContact(models.Model):
    replier = models.CharField(max_length=100)
    contact = models.ForeignKey(ContactUs, on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=200, default='Reply Contacts')
    message = models.TextField()
    attachment = models.FileField(upload_to='contact-attchments', default='empty-profile.png')
    created_at = models.DateTimeField(default=datetime.now())
    
    
    class  Meta:
        verbose_name_plural = 'ReplyContact'
        ordering = ['-created_at']
        
        
    def __str__(self):
        return f'{self.replier} : {self.message[:30]}'


class Subscribe(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(default=datetime.now())
    class  Meta:
        verbose_name_plural = 'Subscribe'
        ordering = ['-created_at']
        
    def __str__(self):
        return f'{self.email}'


class SendNewsletter(models.Model):
    letter = models.TextField()
    attachment = models.FileField(upload_to='newsletter-file', default='empty-profile.png')
    sender = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    class  Meta:
        verbose_name_plural = 'SendNewsletter'
        ordering = ['-created_at']
        
    def __str__(self):
        return f'{self.letter[:50]}'
    
    
    