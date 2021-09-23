from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_email_task


# Create your views here.
def index(request):
    send_email_task.delay()
    # sleepy.delay(10)
    return HttpResponse('<h1>EMAIL HAS BEEN SENT WITH CELERY!</h1>')

