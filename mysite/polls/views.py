from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from polls.models import Poll, Choice
from django.views import generic

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_poll_list"

    def get_queryset(self):
        """Return the last five published polls"""
        return Poll.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Poll
    template_name = "polls/details.html"

class ResultsView(generic.DetailView):
    model = Poll
    template_name = "polls/results.html"

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk = poll_id)

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




