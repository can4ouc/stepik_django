from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.
from django.template import loader

from .forms import AskForm, AnswerForm
from .models import Question


def question(request, num, ):
    try:
        q = Question.objects.get(id=num)
    except Question.DoesNotExist:
        raise Http404
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            _ = form.save()
            url = q.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': q.id})

    return render(request, 'question.html', {'question': q,
                                             'form': form,
                                             'user': request.user,})


def index(request):
    try:
        page = int(request.GET.get("page"))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    questions = Question.objects.all().order_by('-pk')
    paginator = Paginator(questions, 10)
    page = paginator.page(page)

    return render(request, 'list.html',
                  {'title': 'Latest',
                   'paginator': paginator,
                   'questions': page.object_list,
                   'page': page, })


def popular(request):
    try:
        page = int(request.GET.get("page"))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    questions = Question.objects.all().order_by('-rating')
    paginator = Paginator(questions, 10)
    page = paginator.page(page)

    return render(request, 'list.html',
                  {'title': 'Popular',
                   'paginator': paginator,
                   'questions': page.object_list,
                   'page': page, })


def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            post = form.save()
            url = post.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form,
                                        'user': request.user,
                                        })


