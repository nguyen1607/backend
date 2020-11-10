from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello')
# Create your views here.
def detail(request, question_id):
    return HttpResponse('You look at question %s' % question_id)

def results(request, question_id):
    respone = 'You look at the results %s'
    return HttpResponse(respone % question_id)
    
def vote(request, question_id):
    return HttpResponse('You vote on question %s' % question_id)