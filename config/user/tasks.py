from celery import shared_task

@shared_task
def send_email(email, otp):
    print("Here are sending email")
    print(email, otp)