# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages

from models import *

def noname(req):
    return 'id' not in req.session

def index(req):
    return render(req, "regis/index.html")

def login(req):
    result = User.manager.login(req.POST)
    if result[0]:
        req.session['id'] = result[1].id
        # print req.session['id']
        return redirect('/success')
    for key, message in result[1].iteritems():
        messages.error(req,message)
    return redirect('/')

def register(req):
    result = User.manager.createUser(req.POST)
    if result[0]:
        return redirect('/success')
    for key, message in result[1].iteritems():
        messages.error(req, message)
    return redirect('/')

def success(req):
    if noname(req):
        return redirect('/')
    user = User.manager.get(id=req.session['id'])
    context={
        'self': user
    }
    return render(req, "regis/success.html", context)

def logout(req):
    req.session.clear()
    return redirect('/')
# Create your views here.
