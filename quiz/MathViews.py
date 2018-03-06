from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.models import  User, Group
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

correct = "Right Answer!"
incorrect = "Wrong Answer!"
correctb4 = "Right Answer! But you solved that before! Solve something new!"

@login_required
def MathList(request):
	queryset = MathTopic.objects.all().order_by('id')

	context = {
		"object_list" : queryset,
		"title" : "Math Topics"
	}

	return render(request, "subject/index.html", context)

@login_required
def MathTopicDetail(request, slug):
	topic = get_object_or_404(MathTopic, slug=slug)
	queryset = MathSet.objects.filter(topic = topic.id)

	context = {
		"title" : topic.name,
		"topic" : topic,
		"object_list" : queryset
	}

	return render(request, "subject/topic.html", context)

@login_required
def MathSetDetail(request, topic, pk):
	thisSet = get_object_or_404(MathSet, pk = pk)
	queryset = MathQuestion.objects.filter(belongsTo = thisSet.id).order_by('id')
	solved = MathAnswer.objects.filter(solver =  request.user)
	
	solvedset = []

	for q in solved:
		solvedset.append(q.question.id)


	context = {
		"object_list" : queryset,
		"solved_list" : solvedset,
		"title" :  topic.title() + ": " + thisSet.name,
	}

	return render(request, "subject/questions.html", context)

@login_required
def MathQuestionDetail(request, topic, id, pk):
	instance = get_object_or_404(MathQuestion, pk = pk)
	user = get_object_or_404(UserDetail, user = request.user)
	solved = MathAnswer.objects.filter(solver = request.user, question = instance)

	if request.method == "POST":
		userAnswer = request.POST["option"]
		if userAnswer == instance.answer:
			if not solved:
				user.score = user.score + instance.points
				user.save()
				messages.success(request, correct)
				MathAnswer.objects.create(solver = request.user.username, question = instance)
			else:
				messages.success(request, correctb4)
		else:
			messages.success(request, incorrect)

	def get_next():
		next = MathQuestion.objects.filter(pk__gt=pk)
		if next:
			return next.first().id
		return False
	if get_next():
		next = get_next()
	else:
		next = ''

	def get_prev():
		prev = MathQuestion.objects.filter(pk__lt=pk).order_by('-id')
		if prev:
		  return prev.first().id
		return False
	if get_prev():
		prev = get_prev()
	else:
		prev = ''

	context = {
		"title" : instance.question,
		"object" : instance,
		"next" : next,
		"prev" : prev,
	}
	return render(request, "subject/detail.html", context)