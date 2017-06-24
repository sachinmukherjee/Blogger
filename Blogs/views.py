# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response, render
from django.template import RequestContext

from .models import Blogs, Login, User


def home(request):
    blog = Blogs.objects.all()
    return render_to_response('home.html', {'results': blog})


def login(request):
    if request.GET.get('login'):
        email = request.GET.get('email')
        # password = request.GET['password']
        log = Login.objects.all()
        for auth in log:
            if email == auth.email:
                return render_to_response('home.html', {})
            else:
                error = True
                return render_to_response('register.html', {'error': True})
    else:
        return render_to_response('login.html')


def register(request):
    if request.GET.get('submit'):
        password1 = request.GET.get('password')
        password2 = request.GET.get('password2')
        if password1 == password2:
            email = request.GET.get('email')
            user = Login(email=email, password=password1)
            user.save()
            return render_to_response('home.html')
        else:
            return render_to_response('register.html', {'success': True})
    else:
        render_to_response('register.html', {'error': True})
