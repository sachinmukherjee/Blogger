# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from tinymce.models import HTMLField


class Login(models.Model):
    email = models.EmailField()
    password = models.TextField(max_length=20)

    def __str__(self):
        return "%s %s" % (self.id, self.email)


class User(models.Model):
    fullname = models.CharField(max_length=30)
    description = models.TextField(max_length=50)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    email = models.EmailField()
    login_id = models.ForeignKey(Login)

    def __str__(self):
        return "%s %s %s %s %s %s " % (self.id, self.fullname, self.city, self.country, self.country, self.login_id)


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField("DATE", default=datetime.date.today)
    username = models.ForeignKey(User)

    def __str__(self):
        return " %s %s %s %s " % (self.title, self.content, self.date, self.username.fullname)


class Saved(models.Model):
    blog_id = models.ForeignKey(Blogs)
    user_id = models.ForeignKey(User)

    def __str__(self):
        return "%s %s" % (self.blog_id, self.user_id)


class ReadLater(models.Model):
    blog_id = models.ForeignKey(Blogs)
    user_id = models.ForeignKey(User)

    def __str__(self):
        return "%s %s" % (self.blog_id, self.user_id)