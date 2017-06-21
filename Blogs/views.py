# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from . models import Blogs, Login, User


def home(request):
    blog = Blogs.objects.all()
    return render_to_response('home.html', {'results': blog})


def login(request):
    return render_to_response('login.html')