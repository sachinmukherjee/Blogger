# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date


class Login(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)

    def __str__(self):
        return "%s %s" % (self.email, self.password)


class Users(models.Model):
    fullname = models.CharField(max_length=50,primary_key=True)
    description = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    login_id = models.ForeignKey(Login)

    def __str__(self):
        return "%s %s %s %s %s" % (self.fullname, self.description, self.state, self.city, self.country)


class Blogs(models.Model):
    title = models.CharField(max_length=40, primary_key=True)
    content = models.TextField()
    date = models.DateField("Date", default=date.today)
    user_name = models.ForeignKey(Users)

    def __str__(self):
        return '%s %s %s %s' % (self.title, self.content, self.date, self.user_name)


class Saved(models.Model):
    title = models.ForeignKey(Blogs)

    def __str__(self):
        return self.title


class ReadLater(models.Model):
    title = models.ForeignKey(Blogs)

    def __str__(self):
        return self.title
