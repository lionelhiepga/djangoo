from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):
    return render(request, 'luachon/base.html')

def xemds_question(request):
    lst = Question.objects.all()
    context = {"ds_quest": lst}
    return render(request, "luachon/questionlist.html", context)

def detail(request, question_id):
    q = Question.objects.get(pk = question_id)
    return render(request, "luachon/detail_question.html", {'qs': q})

def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." % question_id)    
    q = Question.objects.get(pk = question_id)
    try:
        dulieu = request.POST["dvc"]
        c = q.choice_set.get(pk = dulieu)
    except:
        HttpResponse("lỗi không có choice !!!")
    c.vote = c.vote + 1
    c.save()
    return render(request, "luachon/result.html", { "q": q })

