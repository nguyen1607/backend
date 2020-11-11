from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from app1.models import Choice, Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('app1/index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'app1/index.html', context)
# Create your views here.
def detail(request, question_id):
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'app1/detail.html', {'question':question})

def results(request, question_id):
    respone = 'You look at the results %s'
    return HttpResponse(respone % question_id)
    
def vote(request, question_id):
    return HttpResponse('You vote on question %s' % question_id)
