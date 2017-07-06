# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from .models import Blogs, Login, User, Saved, ReadLater


@csrf_exempt
def home(request):
    blog = Blogs.objects.all().order_by('-date')
    if request.session["login_user"]:
        log = Login.objects.get(pk=request.session["login_user"])
        user = User.objects.get(login_id=log)
        readlater = ReadLater.objects.filter(user_id=user).count()
        saved = Saved.objects.filter(user_id=user).count()
        return render_to_response('home.html', {'blogs': blog, 'readlater': readlater, 'save': saved})
    else:
        return render_to_response('home.html', {'blogs': blog, 'readlater': 0, 'save': 0})


@csrf_exempt
def login(request):
    return render_to_response('login.html')


@csrf_exempt
def loginValidation(request):
    if request.POST.get('login') and request.POST.get("password") and request.POST.get("email"):
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
    else:
        return HttpResponseRedirect("/login/")


@csrf_exempt
def register(request):
    return render_to_response('register.html')


@csrf_exempt
def addUser(request):
    if request.POST.get('submit') and request.POST.get('email') and request.POST.get('password') and request.POST.get(
            'password2'):
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
    try:
        if request.session["login_user"]:
            blog = Blogs.objects.get(pk=blogs_id)
            return render_to_response('individualblog.html', {'individual': blog})
        else:
            return HttpResponseRedirect("/login/")
    except KeyError:
        return HttpResponseRedirect("/login/")


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
    if request.session["login_user"]:
        if request.session["blog_user"]:
            return render_to_response("publish.html", {})
        else:
            return HttpResponseRedirect("/register/addUser/")
    else:
        return HttpResponseRedirect("/login/")


def addContent(request):
    if request.GET.get("submit") == "submit":
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


def logout(request):
    if request.session["login_user"] or request.session["blog_user"]:
        request.session["login_user"] = False
        request.session["blog_user"] = False
        return HttpResponseRedirect("/home/")
    else:
        return HttpResponseRedirect("/home/")


def profile(request):
    if request.session["login_user"]:
        user = request.session["login_user"]
        log = Login.objects.get(pk=user)
        usr = User.objects.get(login_id=log)
        return render_to_response("profile.html", {"User": usr})
    else:
        return HttpResponseRedirect("/login/")


def saved(request):
    if request.session["login_user"]:
        user = request.session["login_user"]
        log = Login.objects.get(pk=user)
        usr = User.objects.get(login_id=log)
        save = Saved.objects.get(user_id=usr)
        return render_to_response("saved.html", {"Saved": save})
    else:
        return HttpResponseRedirect("/login/")


def readlater(request):
    if request.session["login_user"]:
        user = request.session["login_user"]
        log = Login.objects.get(pk=user)
        usr = User.objects.get(login_id=log)
        readlater = ReadLater.objects.get(user_id=usr)
        return render_to_response("readlater.html", {"Read": readlater})
    else:
        return HttpResponseRedirect("/login/")

@csrf_exempt
def read(request):
    if request.session["login_user"]:
        value = request.POST.get("submit")
        blog = Blogs.objects.get(pk=value)
        try:
            ReadLater.objects.get(blog_id=blog)
            return HttpResponseRedirect("/home/")
        except DoesNotExist:
            log = Login.objects.get(pk=request.session["login_user"])
            user = User.objects.get(login_id=log)
            reads = ReadLater()
            reads.blog_id = blog
            reads.user_id = user
            reads.save()
            return HttpResponseRedirect("/home/")
    else:
        return HttpResponseRedirect("/login/")

@csrf_exempt
def save(request):
    value = request.POST.get("submit")
    blog = Blogs.objects.get(pk=value)
    try:
        Saved.objects.get(blog_id=blog)
        return HttpResponseRedirect("/home/")
    except DoesNotExist:
        log = Login.objects.get(pk=request.session["login_user"])
        user = User.objects.get(login_id=log)
        sav = Saved()
        sav.blog_id = blog
        sav.user_id = user
        sav.save()
        return HttpResponseRedirect("/home/")
