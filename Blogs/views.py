# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from .models import Blogs, Login, User

@csrf_exempt
def home(request):
    blog = Blogs.objects.all().order_by('date')
    return render_to_response('home.html', {'blogs': blog})

@csrf_exempt
def login(request):
    return render_to_response('login.html')


@csrf_exempt
def loginValidation(request):
    email = request.POST.get('email')
    log = Login.objects.filter(email=email).first()
    if log:
        user = Login.objects.get(email=email)
        request.session["login_user"] = user.pk
        user1 = User.objects.get(login_id=user)
        request.session['blog_user'] = user1.pk
        return HttpResponseRedirect("/home/")
    else:
        return HttpResponseRedirect('/register/')


@csrf_exempt
def register(request):
    return render_to_response('register.html')


@csrf_exempt
def addUser(request):
    if request.POST.get('submit'):
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password1 == password2:
            email = request.POST.get('email')
            user = Login()
            user.email = email
            user.password = password1
            user.save()
            foreign = Login.objects.get(email=email)
            request.session["login_user"] = foreign.pk
            return HttpResponseRedirect('/details/')
        else:
            return HttpResponseRedirect('/register/')
    else:
        return HttpResponseRedirect('/home/')

@csrf_exempt
def blogs(request, blogs_id):
    blog = Blogs.objects.get(pk=blogs_id)
    return render_to_response('individualblog.html', {'individual': blog})

@csrf_exempt
def details(request):
    return render_to_response('adduser.html')

@csrf_exempt
def detailProcessing(request):
    if request.GET.get('submit') == "submit":
        fullname = request.GET.get('fullname')
        description = request.GET.get('description')
        city = request.GET.get('city')
        state = request.GET.get('state')
        country = request.GET.get('country')
        email = request.GET.get('email')
        usr = request.session["login_user"]  # for getting saved session variable login
        log = Login.objects.get(pk=usr)  # to get all details for the users
        user = User()
        user.fullname = fullname
        user.description = description
        user.city = city
        user.state = state
        user.country = country
        user.email = email
        user.login_id = log
        user.save()
        user_foriegn = User.objects.get(fullname=fullname)
        request.session["blog_user"] = user_foriegn.pk
        return HttpResponseRedirect('/home/')
    else:
        return HttpResponseRedirect('/details/')


def publish(request):
    render_to_response('publish.html')


def addContent(request):
    if request.GET.get("submit"):
        title = request.GET.get("title")
        content = request.GET.get("content")
        usr = request.session["blog_user"]
        user = User.objects.get(pk=usr)
        blog = Blogs()
        blog.title = title
        blog.content = content
        blog.username = user
        blog.save()
        return HttpResponseRedirect('/home/')
    else:
        return HttpResponseRedirect('/publish/')
