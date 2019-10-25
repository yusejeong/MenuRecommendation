from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

#from django.template import loader

from .models import Question, Choice

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')

#     context = {
#         'latest_question_list' : latest_question_list,
#     }
#     # return render(request, 'polls/index.html', context)
#     return HttpResponse(template.render(context, request))

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk = question_id)
#     except:
#         raise Http404("Question dose not exist")
    
#     # question = get_objext_or_404(Question, pk = question_id)

#     return render(request, 'polls/detail.html', {'question' : question})

#     # return HttpResponse("You're looking at question %s." % question_id)

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def results(request, question_id):
#     question = get_object_or_404(Question, pk = question_id)
#     return render(request, 'polls/results.html', {'question' :question})

#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response %question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

    # return HttpResponse("You're voting on question %s." % question_id)