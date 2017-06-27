# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . models import Login, Blogs, User

admin.site.register(Login)
admin.site.register(Blogs)
admin.site.register(User)