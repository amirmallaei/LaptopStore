from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
@shared_task
def send_email(email, otp):
    settings.REDIS_INSTANCE.set(f"{otp}", email, ex=180)

    link = f"http://0.0.0.0:8000/users/activate/{otp}/"

    html_content = render_to_string('email/send_token.html', {"link": link})

    msg = EmailMultiAlternatives(
        subject='Activate Your Account',
        from_email='amirmallaei@gmail.com',
        to=[email]
    )

    msg.attach_alternative(html_content, "text/html")

    msg.send()


