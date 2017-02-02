from django.shortcuts import render
from django.http import Http404
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm, SignUpForm, LoginForm

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

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
    try:
        questions = paginator.page(page)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

#    questions = paginator.page(page) # Page
    return render(request, 'all.html', {
        'questions': questions,
        'baseurl' : reverse(url_name),
})


def question(request, *args, **kwargs):
    id=int(kwargs['id'])
    try:
        question = Question.objects.get(pk=id)
    except Question.DoesNotExist:
        raise Http404
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.cleaned_data['author']=request.user
            ans=form.save()
            return HttpResponseRedirect('/question/%d/' % id)

    answers=Answer.objects.filter(question__pk=id)
    form = AnswerForm()
    return render(request, 'question.html', {
        'question': question,
        'answers': answers,
        'form':form,
    })

def ask(request, *args, **kwargs):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            form.cleaned_data['author']=request.user
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'askform.html', {
        'form': form
    })
# --------------------------------------
from django.contrib.auth import authenticate, login

def signup(request, *args, **kwargs):
    if request.method == "POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=User.objects.create_user(**form.cleaned_data)
            login(request, user)
            request.session.create()
            return HttpResponseRedirect('/')
    form=SignUpForm()
    return render(request, 'signupform.html', {
        'form': form,
    })


def login(request, *args, **kwargs):
    if request.method != "POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user:
                login(request,user)
                request.session.create()
                return HttpResponseRedirect('/')
    form=LoginForm()
    return render(request, 'loginform.html', {
        'form': form,
    })
