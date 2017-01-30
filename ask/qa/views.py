from django.shortcuts import render
from django.http import Http404
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from qa.models import Question, Answer

# Create your views here.
from django.http import HttpResponse

def test(request, *args, **kwargs):
    return HttpResponse('OK', status=200)

def all(request):
    return show(request,Question.objects.new(),'question-all')

def popular(request):
    return show(request,Question.objects.popular(),'question-popular')


# new questions view
def show(request, query, url_name):
    limit = 10 # hadrcoding!!!
    page = request.GET.get('page', 1) #hardcoding !!!
    paginator = Paginator(query, limit)
#    paginator.baseurl = reverse(url_name)
    questions = paginator.page(page) # Page
    return render(request, 'all.html', {
        'questions': questions,
        'baseurl' : reverse(url_name),
})

def question(request, *args, **kwargs):
    try:
        question = Question.objects.get(pk=kwargs['id'])
    except Question.DoesNotExist:
        raise Http404
    answers=Answer.get_by_id(kwargs['id'])
    return render(request, 'question.html', {
        'question': question,
        'answers': answers
    })