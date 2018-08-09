from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import *
from django.template import RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.core.mail import EmailMessage
from smtplib import SMTPRecipientsRefused
from django.utils.html import format_html
from django.template.loader import get_template
from django.template import Context


def sender(request, name):
    obj = Cont.objects.filter(name=name)[0]
    return render(
        request,
        'photos/photos.html',
        context={
            'obj': obj,
            'btt_link': reverse('photos:manage'),
            'thanks_link': reverse('photos:thanks', args=(name,))
        }
    )


def manage(request):
    address = request.POST['mailaddress']
    name = request.POST['objname']
    obj = Cont.objects.filter(name=name)[0]
    print('WYSYŁANIE')
    template = get_template('photos/email.html')
    #context = Context({'link': obj.link})
    content = template.render({'obj': obj})
    try:
        email = EmailMessage('Asia i Karol - zdjęcia', content, from_email='Asia&Karol <asiaandkarol@gmail.com>', to=[address])
        email.content_subtype = 'html'
        email.send()
    except SMTPRecipientsRefused as err:
        print('Nie wysłano bo wystąpił błąd najprawdopodobniej adresu:  \n%s' % err)
    return HttpResponse('')


def thanks(request, name):
    obj = Cont.objects.filter(name=name)[0]
    return render(
        request,
        'photos/thanks.html',
        context={'obj': obj}
    )


def mail(request, name):
    obj = Cont.objects.filter(name=name)[0]
    return render(
        request,
        'photos/email.html',
        context={
            'obj': obj
        }
    )
