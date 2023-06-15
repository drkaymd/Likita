from django.contrib import admin
from .models import ContactUs,ReplyContact, Subscribe,SendNewsletter
# Register your models here.

admin.site.register(ContactUs)
admin.site.register(ReplyContact)
admin.site.register(Subscribe)
admin.site.register(SendNewsletter)
