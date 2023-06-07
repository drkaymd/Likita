from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings

from django.core.mail import EmailMessage, get_connection
from base.models import User, Post
from .forms import ProfileForm, ReplyForm, ContactForm
from .models import ContactUs, ReplyContact


# Create your views here.

def profile(request, pk):
    user_profile = User.objects.get(username=pk)
    # avatar = request.FILES.get('avatar')
    form = ProfileForm(instance=user_profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'user_profile': user_profile, 'form': form}
    return render(request, 'profiles/profile.html', context)


def about_me(request, pk):
    aboutMe = User.objects.get(username=pk)

    context = {'aboutMe': aboutMe}
    return render(request, 'profiles/about-me.html', context)


def gallery(request):
    posts = Post.objects.all()

    context = {'posts': posts}
    return render(request, 'profiles/gallery.html', context)


def contact_me(request):
    contact_us = ContactUs.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = ContactUs.objects.create(
            name=name, email=email, subject=subject, message=message)
    
        mail = EmailMessage(subject=contact.subject, body=contact.message, from_email=contact.email, to=[settings.EMAIL_HOST_USER])
        mail.send()
        
        messages.success(
            request, f'Dear {contact.name}, We have gotten your message. We will respond to your query within 24hours')
    context = {'contact_us': contact_us}
    return render(request, 'profiles/contacts.html', context)
    
   
def reply_contacts(request, pk):
    form = ReplyForm()
    if ContactUs.objects.filter(id=pk).exists():
        contact = ContactUs.objects.get(id=pk)
    else:
        return HttpResponse("Not contact message exists")
    
    if request.user.is_superuser:
            replier = request.user.username
    else:
        messages.warning(request, "Action Denied")
        return redirect('profile', pk=request.user.username)
    if request.method == "POST":
        subject = request.POST['subject']
        message = request.POST['message']
        attach = request.FILES['attachment']
        
        reply = ReplyContact.objects.create(
        replier = replier,
        contact = contact,
        subject =subject,
        message = message,
        attachment = attach
        )
        from_mail = settings.EMAIL_HOST_USER
        to_mail = contact.email
                           
        if from_mail and to_mail:
            try:
                mail = EmailMessage(subject=reply.subject, body=reply.message, from_email=from_mail, to=[to_mail],
                                    )
                mail.attach(attach.name, attach.read(), attach.content_type)
                mail.send()
            except ArithmeticError as aex:
                return HttpResponse('Invalid header found')
            return HttpResponseRedirect('/mail/thanks/')
        # else:
        #     return HttpResponse('Make sure all fields are entered and valid.')
            
       
    else:
        form = ReplyForm()    
        context = {'form': form, 'contact': contact}
    
        return render(request, 'profiles/reply-contacts.html', context)
