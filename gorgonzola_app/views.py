from .models import Log
from django.shortcuts import render
from datetime import datetime


def index(request):
    now = datetime.utcnow()
    log = Log.objects.last()
    if log and log.created_on.date() == now.date():
        status = log.status
    else:
        status = False

    context = {'gorzongola_status': status}
    return render(request, 'gorgonzola_app/index.html', context)


def about(request):
    return render(request, 'gorgonzola_app/about.html')


def subscription(request):
    return render(request, 'gorgonzola_app/subscription.html')
