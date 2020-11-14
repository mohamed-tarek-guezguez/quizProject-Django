from django.shortcuts import render, redirect
from urlparams.redirect import param_redirect
from .models import Questions1, Questions2
from django.contrib import messages
from django.conf import settings

# Create your views here.
def index(request):

    Questions = Questions1.objects.all()
    count = Questions1.objects.all().count()

    listOfTrue = []
    for Question in Questions:
        listOfTrue.append(Question.answer)

    option = []
    if request.method == 'POST':
        for Question in Questions:
            option.append(request.POST['op' + str(Question.nbr)])
            result = len([i for i, j in zip(listOfTrue, option) if i == j])

        if int(count*0.7) <= result:
            messages.info(request, 'You Have ' + str(result) + ' / ' + str(count))
            return redirect('secondQuiz')
        else:
            messages.info(request, 'You Have' + str(result) + ' / ' + str(count))
            return redirect('result')

    context = {
        'Questions': Questions,
        'count': count,
    }

    return render(request, 'firstQuiz.html', context)

def secondQuiz(request):

    Questions = Questions2.objects.all()
    count = Questions2.objects.all().count()

    listOfTrue = []
    for Question in Questions:
        listOfTrue.append(Question.answer)

    option = []
    if request.method == 'POST':
        for Question in Questions:
            option.append(request.POST['op' + str(Question.nbr)])
            result = len([i for i, j in zip(listOfTrue, option) if i == j])

        if int(count*0.7) <= result:
            messages.info(request, 'You Have ' + str(result) + ' / ' + str(count))
            return redirect('win')
        else:
            messages.info(request, 'You Have' + str(result) + ' / ' + str(count))
            return redirect('result')

    context = {
        'Questions': Questions,
        'count': count,
    }
    return render(request, 'secondQuiz.html', context)

def result(request):
    context = {

    }
    return render(request, 'result.html', context)

def win(request):
    context = {

    }
    return render(request, 'win.html', context)
