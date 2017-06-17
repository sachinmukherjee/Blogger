# -*- coding: utf-8 -*-


from django.contrib import admin
from . models import Users,Blogs,Saved,ReadLater,Login

admin.site.register(Users)
admin.site.register(Blogs)
admin.site.register(Saved)
admin.site.register(ReadLater)
admin.site.register(Login)
