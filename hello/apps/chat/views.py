from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from django.urls import reverse
from django.conf import settings
from django.views.generic import View
from .forms import FeedBackForm

def contact(request):
    if request.method == "POST":
        form = FeedBackForm(request.POST)
        if form.is_valid():
            send_mail(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['description'], 'admiralgeneral2003@gmail.com', ['admiralgeneral2003@gmail.com'], fail_silently=False)
            return redirect('/home/comment/')
    else:
        form = FeedBackForm()
    return render(request, "chat/comment.html", {'form':form})