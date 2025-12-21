import os
os.environ['DEBUG'] = 'False'
os.environ['DJANGO_SETTINGS_MODULE'] = 'camerainstallationweb.settings'
import django
django.setup()

from django.test import Client
from home.models import QuoteMessage

print('🔄 Testing actual email sending (SMTP backend)...')

# Test quote form with actual SMTP sending
client = Client()
response = client.post('/request-quote/', {
    'full_name': 'Tashinga Munqitshwa',
    'email': 'munqitshwatashinga1@gmail.com',
    'phone': '0786395484',
    'service': 'camera',
    'message': 'Test email - please check your Gmail inbox! This should be sent via SMTP.'
})

print('✅ Quote form POST status:', response.status_code)
print('✅ Quote messages in DB:', QuoteMessage.objects.count())
print('📧 Email should now be in your Gmail inbox!')
print('📧 Check spam folder if you don\'t see it in inbox')