# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, World. You are at the polls index!')

def detail(request, question_id):
    return HttpResponse('You are looking at question %s.' %question_id)

def results(request, question_id):
    result = "You're looking at the results of question %s."
    return HttpResponse(result %question_id)

def vote(request, question_id):
    return HttpResponse('You are voting for question %s.' %question_id)
