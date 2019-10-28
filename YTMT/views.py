from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

#from django.template import loader

from .models import User

# Create your views here.

class SignInView():
    template_name = 'user/signin.html'

class SignInCompleteView():
    template_name = 'user/signincomplete.html'


class SignUpView():
    template_name = 'user/signup.html'

class BirthandGenderView():
    template_name = 'user/birthandgender.html'

class ReligionView():
    template_name = 'user/religion.html'

class AllergieView():
    template_name = 'user/allergie.html'

class VegetarianView():
    template_name = 'user/vegetarian.html'

class HatelistView():
    template_name = 'user/hatelist.html'

class SignUpCompleteView():
    template_name = 'user/signupcomplete.html'


class FindInfoView():
    template_name = 'user/findinfo.html'

class FindIDView():
    template_name = 'user/findid.html'

class IDInfoView():
    template_name = 'user/idinfo.html'

class FindPWView():
    template_name = 'user/findpw.html'

class SendPWView():
    template_name = 'user/sendpw.html'


class MypageView():
    template_name = 'mypage/mypage.html'

class EditInforView():
    template_name = 'mypage/editinfo.html'

class EditMoreInfoView():
    template_name = 'mypage/editmoreinfo.html'

class EditReligionView():
    template_name = 'user/religion.html'

class EditAllergieView():
    template_name = 'user/allergie.html'

class EditVegetarianView():
    template_name = 'user/vegetarian.html'

class EditHatelistView():
    template_name = 'user/hatelist.html'

class HistoryView():
    template_name = 'mypage/history.html'

class FriendlistView():
    template_name = 'mypage/friendlist.html'









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