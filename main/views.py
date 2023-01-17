from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.

def homepage(request):
    return render(request, 'main/home.html')

def question1(request):
    question1 = Question.objects.get(pk=1)

    user_input = request.POST.get('question1')
    answer1 = Question.objects.values_list('answer', flat=True).get(pk=1)

    if user_input == answer1:
        print('CORRECT')
        return redirect('home')
    else:
        print('WRONG TANIGNANG BUHAY TO')

    context = {'question1':question1}
    return render(request, 'main/question1.html', context)

def question2(request):
    question2 = Question.objects.get(pk=2)

    user_input = request.POST.get('question2')
    answer2 = Question.objects.values_list('answer', flat=True).get(pk=2)

    if user_input == answer2:
        print('CORRECT')
        return redirect('home')
    else:
        print('WRONG TANIGNANG BUHAY TO')

    context = {'question2':question2}
    return render(request, 'main/question2.html', context)


def question3(request):
    question3 = Question.objects.get(pk=3)

    user_input = request.POST.get('question3')
    answer3 = Question.objects.values_list('answer', flat=True).get(pk=3)

    if user_input == answer3:
        print('CORRECT')
        return redirect('home')
    else:
        print('WRONG TANIGNANG BUHAY TO')

    context = {'question3':question3}
    return render(request, 'main/question3.html', context)

