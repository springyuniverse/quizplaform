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
	
	correctlySolvedSet = []
	incorrectlySolvedSet = []

	for q in solved:
		if q.state == True: 
			correctlySolvedSet.append(q.question.id)
		elif q.state == False:
			incorrectlySolvedSet.append(q.question.id)

	context = {
		"object_list" : queryset,
		"correctly_solved_list" : correctlySolvedSet,
		"incorrectly_solved_list" : incorrectlySolvedSet,
		"title" :  topic.title() + ": " + thisSet.name,
	}

	return render(request, "subject/questions.html", context)

@login_required
def MathQuestionDetail(request, topic, id, pk):
	thisSet = get_object_or_404(MathSet, pk = pk)
	queryset = MathQuestion.objects.filter(belongsTo = thisSet.id).order_by('id')

	instance = get_object_or_404(MathQuestion, id = id)
	user = get_object_or_404(UserDetail, user = request.user)
	solved = MathAnswer.objects.filter(solver = request.user, question = instance, state = True)

	# Storing exact answers alongside true and false in order to use it for analytical purposes in the future
	# Wird die bestimmte Antworten neben richtig und falsch gespeichert, um fur analytische Zwecken in der Zukunft zu benutzen. 

	if request.method == "POST":
		userAnswer = request.POST["option"]
		if userAnswer == instance.answer:
			if not solved:
				user.score = user.score + instance.points
				user.save()
				messages.success(request, correct)
				MathAnswer.objects.create(solver = request.user.username, question = instance, answer = userAnswer, state = True)
			else:
				messages.success(request, correctb4)
		else:
			messages.success(request, incorrect)
			MathAnswer.objects.create(solver = request.user.username, question = instance, answer = userAnswer, state = False)

	finished = False

	def get_next():
		next = queryset.filter(id__gt=id)
		if next:
			return next.first().id
		return False
	if get_next():
		next = get_next()
	else:
		next = ''
		total = 0
		for q in queryset:
			if MathAnswer.objects.filter(solver = request.user, question = q):
				total += 1
		finished = True
		request.session['total'] = total
		request.session['outof'] = len(queryset)
		print(total)

	def get_prev():
		prev = queryset.filter(id__lt=id).order_by('-id')
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
		"topic" : thisSet.topic.slug,
		"set" : pk,
		"next" : next,
		"prev" : prev,
		"finished" : finished
	}
	return render(request, "subject/detail.html", context)

def MathProgress(request):
	total = request.session['total']
	outof = request.session['outof']
	context = {
		"total" : total, 
		"outof" : outof
	}
	return render(request, "subject/progress.html", context)

