from django.contrib import admin

# Register your models here.
from .models import EmailSignup

class EmailSignupAdmin(admin.ModelAdmin):
    pass
admin.site.register(EmailSignup, EmailSignupAdmin)