from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from polls.models import Poll, Choice

def index1(request):
    polls = Poll.objects.order_by('-pub_date')[:5]
    template = loader.get_template("polls/index.html")
    context = RequestContext(request, {
        'polls': polls,
    })
    return HttpResponse(template.render(context))

def index(request):
    return render(request,
                  "polls/index.html",
                  { 'polls':  Poll.objects.order_by('-pub_date')[:5] })

def details(request, id):
    poll = get_object_or_404(Poll, pk = id)
    return render(request, "polls/details.html", { 'poll': poll })

def results(request, id):
    poll = get_object_or_404(Poll, pk = id)
    return render(request, "polls/results.html", { 'poll': poll })

def vote(request, id):
    p = get_object_or_404(Poll, pk = id)

    try:
        selection = p.choice_set.get(pk = request.POST['choice'])
    except KeyError, Choice.DoesNotExist:
        return render(request, 'polls/details.html', {
            'poll': p,
            'error_message': "PICK SOMETHING, ASSHOLE"
        })
    else:
        selection.votes += 1
        selection.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))




