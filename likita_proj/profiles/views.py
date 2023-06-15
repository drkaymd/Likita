from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string, get_template
from datetime import datetime, timedelta


from django.core.mail import EmailMessage, get_connection
from base.models import User, Post
from .forms import ProfileForm, ReplyForm, SubscribeForm,NewsletterForm
from .models import ContactUs, ReplyContact, Subscribe, SendNewsletter
from clinic.models import Appointment

# Create your views here.

def profile(request, pk):
    user_profile = User.objects.get(username=pk)    
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime
    #Only show the Appointments 21 days from today
    items = Appointment.objects.filter(day__range=[minDate, maxDate]).order_by('day', 'time')
    appointments = Appointment.objects.filter(name=user_profile.id).order_by('day', 'time')
    form = ProfileForm(instance=user_profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'user_profile': user_profile,
        'form': form, 
        'appointments':appointments,
        'items':items,
        }
    return render(request, 'profiles/profile.html', context)


def about_me(request):
    return render(request, 'profiles/about-me.html')


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
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
            
       
    else:
        form = ReplyForm()    
        context = {'form': form, 'contact': contact}
    
        return render(request, 'profiles/reply-contacts.html', context)


def subscribe(request):
    
    if request.method == "POST":
        from_email = request.POST['newsletter']
        subscription = Subscribe.objects.create(
            email = from_email,
        )
        to_email = settings.EMAIL_HOST_USER      
        from_email = subscription.email
        subscribe_me = EmailMessage(subject="Newsletter Subscription", body='profiles/subscribe.html',
                                            from_email=from_email, to=[to_email])
        subscribe_me.send()
        return redirect('home')



# connection = mail.get_connection()  
# connection.open()   
def send_newsletter(request):
    form = NewsletterForm()
    recipients_mails = Subscribe.objects.all()
    from_mail = settings.EMAIL_HOST_USER
    
    if request.method == "POST":
        form = NewsletterForm(request.POST, request.FILES)
        if form.is_valid():
            letter = form.cleaned_data['letter']
            attach = form.cleaned_data['attachment']
            
        newsletter = SendNewsletter.objects.create(
            sender = request.user if request.user.is_superuser else request.user,
            letter = letter,
            attachment=attach
        )
        html_template = get_template('profiles/newsletter.html')
        context = {'newsletter': newsletter}
        html_content = html_template.render(context)
        for email in  recipients_mails:
            to_mail = email
            mail = EmailMessage(
                subject="Todays Newsletter", 
                body=html_content,
                from_email=from_mail, to=[to_mail]
                )
            mail.attach(attach.name, attach.read(), attach.content_type)
            mail.content_subtype = "html"
            # mail.send()
            # connection.send_messages([mail])
    
    
    context = {'form': form}
    return render(request, 'profiles/send_newsletter.html', context)
# connection.close()

