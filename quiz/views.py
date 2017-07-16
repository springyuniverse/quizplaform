from .models import *
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import *
from django.contrib.auth.models import  User, Group
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
import random
from rest_framework import viewsets
from .serializers import *
from django.contrib.auth.decorators import login_required

correct = "Right Answer!"
incorrect = "Wrong Answer!"
correctb4 = "Right Answer! But you solved that before! Solve something new!"

class MathQuestionViewSet(viewsets.ModelViewSet):
	queryset = MathQuestion.objects.all()
	serializer_class = MathQuestionSerializer

@login_required
def homepage(request):
	user = get_object_or_404(UserDetail, user = request.user)
	score = user.score
	context = {
		"score" : score
	}
	return render(request, "home.html", context)

def register_user(request):
	if request.method == "GET":
		context = {'title' : "Register"}
		return render(request, "register.html", context)
	elif request.method == "POST":
		username = request.POST["username"]
		email = request.POST["email"]
		password = request.POST["password"]

		auth.models.User.objects.create_user(username, email, password).save()
		user = auth.authenticate(username = username, password = password)
		UserDetail.objects.create(user = user)
		login(request, user)
		return redirect("/")

def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/")
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render(request, 'login.html',{'state':state, 'username': username, 'title' : "Login"})

def logout_user(request):
	auth.logout(request)
	return redirect("/login")

class MathListView(generic.ListView):
	template_name = "math/index.html"
	title = "Math"
	def get_queryset(self):
		return MathQuestion.objects.all().order_by('id')

@login_required
def MathDetail(request, pk):
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
	return render(request, "math/detail.html", context)