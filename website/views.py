from django.shortcuts import render,redirect
from .models import Course
from .forms import ContactForm

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'website/contact.html', {'success': True})
    else:
        form = ContactForm()

    return render(request, 'website/contact.html', {'form' : form})
        

def courses(request):

    all_courses = Course.objects.all()

    return render(request, 'website/courses.html', {'courses' : all_courses})

