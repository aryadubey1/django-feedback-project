from django.shortcuts import render,redirect
from .models import Course, Testimonials
from .forms import ContactForm
import requests

def home(request):
    testimonials = Testimonials.objects.all().order_by('-date_posted')[:3]
    return render(request, 'website/home.html', {'testimonials' : testimonials})

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_instance = form.save()

            bot_token ='8485056319:AAGfZm25ZwsQFG3Wb4ieHLkVI2YuApLjSdU'
            chat_id = '1636866465'
            message = (
                f"🔔 *New student Inquiry!*\n\n"
                f"*Name:* {contact_instance.name}\n"
                f"*Subject:* {contact_instance.subject}\n"
                f"*Message:* {contact_instance.message}"
            )

            url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
            payload = {
                'chat_id': chat_id,
                'text': message,
                'parse_mode': 'Markdown'
            }

            try:
                requests.post(url, data=payload)
            except Exception as e :
                print(f"Error sending Telegram message: {e}")


            return render(request, 'website/contact.html', {'success': True})
    else:
        form = ContactForm()

    return render(request, 'website/contact.html', {'form' : form})
        

def courses(request):

    all_courses = Course.objects.all()

    return render(request, 'website/courses.html', {'courses' : all_courses})

