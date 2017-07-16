from django.db import models
from django.contrib.auth.models import  User, Group
from django.core.urlresolvers import reverse


class UserDetail(models.Model):
	name = models.CharField(max_length=50,default="")
	email = models.CharField(max_length=50,default="")
	grade = models.PositiveIntegerField(blank = True, null = True)
	score = models.PositiveIntegerField(default = 1, blank = True, null = True)
	bio = models.TextField(blank = True, null = True)
	user = models.OneToOneField(User)

	def __str__(self):
		return self.user.username

class Exam(models.Model):
	CATEGORIES = (
		('AR', 'Arabic'),
		('MA', 'Math')
	)
	name = models.CharField(max_length = 100, default = "")
	user = models.ForeignKey(User)
	category = models.CharField(max_length = 2, choices = CATEGORIES)

	def __str__(self):
		return self.name;

class MathQuestion(models.Model):
	question = models.TextField(max_length=200,default="")
	option1 = models.CharField(max_length=50,default="")
	option2 = models.CharField(max_length=50, default="")
	option3 = models.CharField(max_length=50, default="")
	option4 = models.CharField(max_length=50, default="")
	answer = models.CharField(max_length=50, default="")
	points = models.PositiveIntegerField()
	exam = models.ForeignKey(Exam, blank = True, null = True)

	def __str__(self):
		return self.question

	def get_absolute_url(self):
		return reverse("math:detail", kwargs={"pk" : self.pk})

class MathAnswer(models.Model):	
	question = models.ForeignKey(MathQuestion, on_delete = models.CASCADE, blank = False)
	solver = models.CharField(max_length = 50)

	def __str__(self):
		return "Answer by: " + self.solver + " on question " + self.question.question
