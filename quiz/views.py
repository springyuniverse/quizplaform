from .models import *
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import *
from django.contrib.auth.models import  User, Group
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

correct = "Right Answer!"
incorrect = "Wrong Answer!"
correctb4 = "Right Answer! But you solved that before! Solve something new!"


@login_required
def homepage(request):
	user = get_object_or_404(UserDetail, user = request.user)

	MathTotal = MathQuestion.objects.all()
	MathSolved = MathAnswer.objects.filter(solver = request.user)
	MathPercent = len(MathSolved)/len(MathTotal)*100
	BiologyTotal = BiologyQuestion.objects.all()
	BiologySolved = BiologyAnswer.objects.filter(solver = request.user)
	BiologyPercent = len(BiologySolved)/len(BiologyTotal)*100
	ChemistryTotal = ChemistryQuestion.objects.all()
	ChemistrySolved = ChemistryAnswer.objects.filter(solver = request.user)
	ChemistryPercent = len(ChemistrySolved)/len(ChemistryTotal)*100
	PhysicsTotal = PhysicsQuestion.objects.all()
	PhysicsSolved = PhysicsAnswer.objects.filter(solver = request.user)
	PhysicsPercent = len(PhysicsSolved)/len(PhysicsTotal)*100
	EnglishTotal = EnglishQuestion.objects.all()
	EnglishSolved = EnglishAnswer.objects.filter(solver = request.user)
	EnglishPercent = len(EnglishSolved)/len(EnglishTotal)*100

	score = user.score
	context = {
		"Math" : MathPercent,
		"Biology" : BiologyPercent,
		"Chemistry" : ChemistryPercent,
		"Physics" : PhysicsPercent,
		"English" : EnglishPercent,
		"score" : score
	}
	return render(request, "home.html", context)

def register_user(request):
	if request.method == "GET":
		context = {'title' : "Register"}
		return render(request, "register.html", context)
	elif request.method == "POST":
		username = request.POST["username"]
		
		if User.objects.filter(username=username).exists():
			messages.success(request, "This username is already taken!")
			return redirect("/register")

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

@login_required
def MathList(request):
	queryset = MathQuestion.objects.all().order_by('id')
	solved = MathAnswer.objects.filter(solver =  request.user)
	solvedset = []

	for q in solved:
		solvedset.append(q.question.id)

	context = {
		"object_list" : queryset,
		"solved_list" : solvedset,
		"title" : "Math",
	}
	return render(request, "subject/index.html", context)

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
	return render(request, "subject/detail.html", context)

@login_required
def BiologyList(request):
	queryset = BiologyQuestion.objects.all().order_by('id')
	solved = BiologyAnswer.objects.filter(solver =  request.user)
	solvedset = []

	for q in solved:
		solvedset.append(q.question.id)

	context = {
		"object_list" : queryset,
		"solved_list" : solvedset,
		"title" : "Biology",
	}
	return render(request, "subject/index.html", context)

@login_required
def BiologyDetail(request, pk):
	instance = get_object_or_404(BiologyQuestion, pk = pk)
	user = get_object_or_404(UserDetail, user = request.user)
	solved = BiologyAnswer.objects.filter(solver = request.user, question = instance)

	if request.method == "POST":
		userAnswer = request.POST["option"]
		if userAnswer == instance.answer:
			if not solved:
				user.score = user.score + instance.points
				user.save()
				messages.success(request, correct)
				BiologyAnswer.objects.create(solver = request.user.username, question = instance)
			else:
				messages.success(request, correctb4)
		else:
			messages.success(request, incorrect)

	def get_next():
		next = BiologyQuestion.objects.filter(pk__gt=pk)
		if next:
			return next.first().id
		return False
	if get_next():
		next = get_next()
	else:
		next = ''

	def get_prev():
		prev = BiologyQuestion.objects.filter(pk__lt=pk).order_by('-id')
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

@login_required
def PhysicsList(request):
	queryset = PhysicsQuestion.objects.all().order_by('id')
	solved = PhysicsAnswer.objects.filter(solver =  request.user)
	solvedset = []

	for q in solved:
		solvedset.append(q.question.id)

	context = {
		"object_list" : queryset,
		"solved_list" : solvedset,
		"title" : "Physics",
	}
	return render(request, "subject/index.html", context)

@login_required
def PhysicsDetail(request, pk):
	instance = get_object_or_404(PhysicsQuestion, pk = pk)
	user = get_object_or_404(UserDetail, user = request.user)
	solved = PhysicsAnswer.objects.filter(solver = request.user, question = instance)

	if request.method == "POST":
		userAnswer = request.POST["option"]
		if userAnswer == instance.answer:
			if not solved:
				user.score = user.score + instance.points
				user.save()
				messages.success(request, correct)
				PhysicsAnswer.objects.create(solver = request.user.username, question = instance)
			else:
				messages.success(request, correctb4)
		else:
			messages.success(request, incorrect)

	def get_next():
		next = PhysicsQuestion.objects.filter(pk__gt=pk)
		if next:
			return next.first().id
		return False
	if get_next():
		next = get_next()
	else:
		next = ''

	def get_prev():
		prev = PhysicsQuestion.objects.filter(pk__lt=pk).order_by('-id')
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

@login_required
def ChemistryList(request):
	queryset = ChemistryQuestion.objects.all().order_by('id')
	solved = ChemistryAnswer.objects.filter(solver =  request.user)
	solvedset = []

	for q in solved:
		solvedset.append(q.question.id)

	context = {
		"object_list" : queryset,
		"solved_list" : solvedset,
		"title" : "Chemistry",
	}
	return render(request, "subject/index.html", context)

@login_required
def ChemistryDetail(request, pk):
	instance = get_object_or_404(ChemistryQuestion, pk = pk)
	user = get_object_or_404(UserDetail, user = request.user)
	solved = ChemistryAnswer.objects.filter(solver = request.user, question = instance)

	if request.method == "POST":
		userAnswer = request.POST["option"]
		if userAnswer == instance.answer:
			if not solved:
				user.score = user.score + instance.points
				user.save()
				messages.success(request, correct)
				ChemistryAnswer.objects.create(solver = request.user.username, question = instance)
			else:
				messages.success(request, correctb4)
		else:
			messages.success(request, incorrect)

	def get_next():
		next = ChemistryQuestion.objects.filter(pk__gt=pk)
		if next:
			return next.first().id
		return False
	if get_next():
		next = get_next()
	else:
		next = ''

	def get_prev():
		prev = ChemistryQuestion.objects.filter(pk__lt=pk).order_by('-id')
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

@login_required
def EnglishList(request):
	queryset = EnglishQuestion.objects.all().order_by('id')
	solved = EnglishAnswer.objects.filter(solver =  request.user)
	solvedset = []

	for q in solved:
		solvedset.append(q.question.id)

	context = {
		"object_list" : queryset,
		"solved_list" : solvedset,
		"title" : "English",
	}
	return render(request, "subject/index.html", context)

@login_required
def EnglishDetail(request, pk):
	instance = get_object_or_404(EnglishQuestion, pk = pk)
	user = get_object_or_404(UserDetail, user = request.user)
	solved = EnglishAnswer.objects.filter(solver = request.user, question = instance)

	if request.method == "POST":
		userAnswer = request.POST["option"]
		if userAnswer == instance.answer:
			if not solved:
				user.score = user.score + instance.points
				user.save()
				messages.success(request, correct)
				EnglishAnswer.objects.create(solver = request.user.username, question = instance)
			else:
				messages.success(request, correctb4)
		else:
			messages.success(request, incorrect)

	def get_next():
		next = EnglishQuestion.objects.filter(pk__gt=pk)
		if next:
			return next.first().id
		return False
	if get_next():
		next = get_next()
	else:
		next = ''

	def get_prev():
		prev = EnglishQuestion.objects.filter(pk__lt=pk).order_by('-id')
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
