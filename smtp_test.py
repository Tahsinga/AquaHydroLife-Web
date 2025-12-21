import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Test SMTP connection and send a test email
try:
    # Create message
    msg = MIMEMultipart()
    msg['From'] = 'munqitshwatashinga1@gmail.com'
    msg['To'] = 'munqitshwatashinga1@gmail.com'
    msg['Subject'] = 'SMTP Test Email'

    body = 'This is a test email to verify SMTP is working.'
    msg.attach(MIMEText(body, 'plain'))

    # Connect to Gmail SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('munqitshwatashinga1@gmail.com', 'qwrugcdidjupquhf')

    # Send email
    text = msg.as_string()
    server.sendmail('munqitshwatashinga1@gmail.com', 'munqitshwatashinga1@gmail.com', text)
    server.quit()

    print('✅ Test email sent successfully! Check your Gmail inbox.')

except Exception as e:
    print('❌ SMTP test failed:', str(e))