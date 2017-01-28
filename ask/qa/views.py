from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from qa.models inport Questions

# Create your views here.
from django.http import HttpResponse 
def test(request, *args, **kwargs):
    return HttpResponse('OK', status=200)

# new questions view
def all(request):
    qw = Questions.objects.new()
    limit = 10 # hadrcoding!!!
    page = request.GET.get('page', 1) #hardcoding !!!
    paginator = Paginator(qw, limit)
    paginator.baseurl = reverse('urls:all')
    page = paginator.page(page) # Page
    return render(request, 'blog/post_by_tag.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
})
