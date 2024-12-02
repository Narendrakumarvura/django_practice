from django.core.mail import send_mail
from django.conf import settings

def send_welcome_email(recipient_email, full_name):
    subject = "Welcome to the Club!"
    message = f"Hello {full_name},\n\nWelcome to our club! We're excited to have you with us.\n\nBest regards,\nThe Club Team"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [recipient_email]

    try:
        send_mail(subject, message, from_email, recipient_list)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
