# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime


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
        return "%s %s %s %s %s " % (self.fullname, self.city, self.country, self.country, self.login_id)


class Blogs(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    content = models.TextField()
    date = models.DateField("DATE", default=datetime.date())
    username = models.ForeignKey(User)

    def __str__(self):
        return "%s %s %s %s " % (self.title, self.content, self.date, self.username)
