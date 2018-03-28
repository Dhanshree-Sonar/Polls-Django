# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = { 'latest_question_list': latest_question_list }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except:
        raise Http404('Question doesn\'t exist!')

    context = { 'question': question }
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    result = "You're looking at the results of question %s."
    return HttpResponse(result %question_id)

def vote(request, question_id):
    return HttpResponse('You are voting for question %s.' %question_id)
