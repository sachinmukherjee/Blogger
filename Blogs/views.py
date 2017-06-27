# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse

from .models import Blogs, Login, User


def home(request):
    blog = Blogs.objects.all()
    return render_to_response('home.html', {'blogs': blog})


@csrf_exempt
def login(request):
    request.method == 'POST'
    email = request.POST.get('email')
    log = Login.objects.filter(email=email).first()
    if log:
        return HttpResponseRedirect("/home/")
    else:
        return HttpResponseRedirect('/register/')


def register(request):
    if request.POST.get('submit'):
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password1 == password2:
            email = request.POST.get('email')
            Log = Login()
            Log.email = email
            if Log.email:
                return render_to_response('login.html')
            else:
                user = Login()
                user.email = email
                user.password = password1
                user.save()
                return render_to_response('home.html')
        else:
            return render_to_response('register.html', {'success': True})
    else:
        return render_to_response('register.html', {'error': True})


def blogs(request, blogs_id):
    blog = Blogs.objects.get(pk=blogs_id)
    return render_to_response('individualblog.html', {'individual': blog})
