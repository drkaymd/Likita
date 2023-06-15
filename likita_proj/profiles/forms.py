from django.forms import ModelForm, ClearableFileInput
from base.models import User
from .models import ReplyContact, ContactUs, Subscribe, SendNewsletter
from django import forms




class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','bio','name','username','date_of_birth','age','gender','email', 'location','profession']
        # fields = '__all__'
        
        
class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        field = '__all__'  
        exclude = ['id', ]  
        
class ReplyForm(ModelForm):
    class Meta:
        model=ReplyContact
        fields = ['subject','message', 'attachment']
        

class SubscribeForm(ModelForm):
    class Meta:
        model =  Subscribe
        fields = ['email']
        
        
class NewsletterForm(ModelForm):
    class Meta:
        model =  SendNewsletter
        fields = ['letter', 'attachment']
        widgets = {
            'attachment': ClearableFileInput(attrs={"allow_multiple_selected": True}),
        }
        
        

# class ReplyForm(forms.Form):
#     email_id = forms.EmailField()
#     email_cc = forms.EmailField()
#     email_bcc = forms.EmailField()
#     subject = forms.CharField(max_length=200)
#     message = forms.CharField(widget=forms.Textarea)
#     attachment = forms.FileField()