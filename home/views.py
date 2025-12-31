from django.shortcuts import render, redirect
import logging
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .models import ContactMessage

logger = logging.getLogger(__name__)

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Save to database
        contact = ContactMessage.objects.create(
            full_name=name,
            email=email,
            phone=phone,
            service='General Inquiry',  # Default service since no service field in form
            message=message
        )

        # Send email notification
        try:
            subject = f'HydroPure Contact Form - New Inquiry'
            body = f"""
New contact form submission from HydroPure website:

Name: {name}
Email: {email}
Phone: {phone}

Message:
{message}
"""
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                ['info@hydropure.co.zw'],  # Updated email
                fail_silently=True,
            )
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
        except Exception as e:
            logger.error(f"Email sending failed: {e}")
            messages.success(request, 'Thank you for your message! We will get back to you soon.')

        return redirect('home')

    return render(request, 'home/index.html')
