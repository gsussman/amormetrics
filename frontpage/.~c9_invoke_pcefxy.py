from django.shortcuts import render, redirect
from signup.forms import EmailSignupForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from formtools.wizard.views import SessionWizardView
from forms import ImageForm, FileFieldForm
from django.views.generic.edit import FormView
from models import Image, ProfileInfo, Age
from amoranalytics import settings
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
        
        
def model_form_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        form2 = request.POST
        for key, values in request.POST.lists():
            print(key, values)
        for key, values in request.FILES.lists():
            print(key, values)
        if form.is_valid():
            print '4'
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            profile = form.cleaned_data['profile']
            a = ProfileInfo(name=name, email=email, texts=profile)
            a.save()
            ages = form2.getlist('age')
            print ages
            for x in ages:
                print x
                y = Age.objects.get(age=x)
                a.age.add(y)
                a.save()
                print a.age
            for f in request.FILES.getlist('image'):
                print 'start'
                b = Image(name=name, email=email, image=f)
                print b
                b.save()
                a.images.add(b)
                print a.images
            a.save()
            return HttpResponseRedirect('OK')
        else:
            print 'form not valid'
            return render(request, 'frontpage/model_form_upload.html', {
            'form': form
            })
    else:
        if request.GET:
            print 'its a get request'
            id = request.GET['id']
            request.session['package'] = id
            print id
        form = ImageForm()
        return render(request, 'frontpage/model_form_upload.html', {
        'form': form
    })

class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'upload.html'  # Replace with your template.
    success_url = '/'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                print (f)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

def signup(request):
    if request.method == "POST":
        form = request.POST
        for key, values in request.POST.lists():
            print(key, values)
        messages.success(request, 'Thank you for signing up! We will be in touch with you shortly.') 
        return HttpResponseRedirect('/signup/')
    else:
    	return render(request, 'frontpage/signup.html')
    	
def payment_form(request):
    context = { "stripe_key": settings.STRIPE_PUBLIC_KEY }
    return render(request, "payments.html", context)