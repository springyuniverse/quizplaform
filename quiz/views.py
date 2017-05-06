from .models import *
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import *
from django.contrib.auth.models import  User, Group
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login

correct = "Right Answer!"
incorrect = "Wrong Answer!"
correctb4 = "Right Answer! But you solved that before! Solve something new!"

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
		return redirect("/dashboard")

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
                return redirect("/db")
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
	def get_queryset(self):
		return MathQuestion.objects.all()

def MathDetail(request, pk):

	instance = get_object_or_404(MathQuestion, pk = pk)
	user = get_object_or_404(UserDetail, user = request.user)
	queryset = MathQuestion.objects.all()
	solved = MathAnswer.objects.filter(solver = request.user, question = instance)

	if request.method == "POST":
		userAnswer = request.POST["option"]
		if userAnswer == instance.answer:
			if not solved:
				user.score = user.score + 1
				user.save()
				messages.success(request, correct)
				MathAnswer.objects.create(solver = request.user.username, question = instance)
			else:
				messages.success(request, correctb4)
		else:
			messages.success(request, incorrect)

	for q in queryset:
		print(q.id)

	context = {
		"title" : instance.question,
		"object" : instance,
	}
	return render(request, "math/detail.html", context)