from django.shortcuts import render
from signup.forms import EmailSignupForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def home(request):

    if request.method == "POST":
        form = EmailSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for signing up! We will let you know when we offically launch!') 
        return HttpResponseRedirect('/')
    else:
    	form = EmailSignupForm()
    	return render(request, 'frontpage/home.html', {'form': form})

def hiw(request):

    if request.method == "POST":
        form = EmailSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for signing up! We will let you know when we offically launch!') 
        return HttpResponseRedirect('/')
    else:
        form = EmailSignupForm()
        return render(request, 'frontpage/hiw.html', {'form': form})

def pricing(request):

    if request.method == "POST":
        form = EmailSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for signing up! We will let you know when we offically launch!') 
        return HttpResponseRedirect('/')
    else:
        form = EmailSignupForm()
        return render(request, 'frontpage/pricing.html', {'form': form})