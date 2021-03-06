from django.db import models
from django.contrib.auth.models import  User, Group
from django.core.urlresolvers import reverse
from multiselectfield import MultiSelectField


class UserDetail(models.Model):
	SUBJECT_OPTIONS = (('MA', 'Math'), ('EN','English'))
	name = models.CharField(max_length=50,default="")
	email = models.CharField(max_length=50,default="")
	grade = models.PositiveIntegerField(blank = True, null = True)
	score = models.PositiveIntegerField(default = 1, blank = True, null = True)
	bio = models.TextField(blank = True, null = True)
	user = models.OneToOneField(User)
	subjects = MultiSelectField(choices = SUBJECT_OPTIONS)

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

### Math ###
class MathTopic(models.Model):
	name = models.CharField(max_length = 200, default = "")
	slug = models.SlugField(unique=True)

	def __str__(self):
		return "Topic: " + self.name

	def get_absolute_url(self):
		return reverse('math:topic', args=[self.slug])

class MathSet(models.Model):
	name = models.CharField(max_length = 200, default = "")
	topic = models.ForeignKey(MathTopic, blank = True, null = True)

	def __str__(self):
		return "Set: " + self.name

	def get_absolute_url(self):
		return reverse("math:set", kwargs={"pk" : self.pk, "topic" : self.topic.slug})

class MathQuestion(models.Model):
	question = models.TextField(max_length=200,default="")
	image = models.CharField(max_length=255, default="", blank = True, null = True)
	option1 = models.CharField(max_length=50,default="")
	option2 = models.CharField(max_length=50, default="")
	option3 = models.CharField(max_length=50, default="")
	option4 = models.CharField(max_length=50, default="")
	answer = models.CharField(max_length=50, default="")
	points = models.PositiveIntegerField()
	belongsTo = models.ForeignKey(MathSet, blank = True, null = True)

	def __str__(self):
		return self.question

	def get_absolute_url(self):
		return reverse("math:detail", kwargs={"id" : self.id, "topic" : self.belongsTo.topic.slug, "pk" : self.belongsTo.id})

class MathAnswer(models.Model):	
	question = models.ForeignKey(MathQuestion, on_delete = models.CASCADE, blank = False)
	solver = models.CharField(max_length = 50)
	answer = models.CharField(max_length = 200, default="", blank= True, null = True)
	state = models.BooleanField()

	def __str__(self):
		return "Answer by: " + self.solver + " on question " + self.question.question


### Biology ###
class BiologyQuestion(models.Model):
	question = models.TextField(max_length=200,default="")
	image = models.CharField(max_length=255,default="", blank = True, null = True)
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
		return reverse("biology:detail", kwargs={"pk" : self.pk})

class BiologyAnswer(models.Model):	
	question = models.ForeignKey(BiologyQuestion, on_delete = models.CASCADE, blank = False)
	solver = models.CharField(max_length = 50)

	def __str__(self):
		return "Answer by: " + self.solver + " on question " + self.question.question

### Physics ###
class PhysicsQuestion(models.Model):
	question = models.TextField(max_length=200,default="")
	image = models.CharField(max_length=255,default="", blank = True, null = True)
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
		return reverse("physics:detail", kwargs={"pk" : self.pk})

class PhysicsAnswer(models.Model):	
	question = models.ForeignKey(PhysicsQuestion, on_delete = models.CASCADE, blank = False)
	solver = models.CharField(max_length = 50)

	def __str__(self):
		return "Answer by: " + self.solver + " on question " + self.question.question

### English ###
class EnglishQuestion(models.Model):
	question = models.TextField(max_length=200,default="")
	image = models.CharField(max_length=255,default="", blank = True, null = True)
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
		return reverse("english:detail", kwargs={"pk" : self.pk})

class EnglishAnswer(models.Model):	
	question = models.ForeignKey(EnglishQuestion, on_delete = models.CASCADE, blank = False)
	solver = models.CharField(max_length = 50)

	def __str__(self):
		return "Answer by: " + self.solver + " on question " + self.question.question

### Chemistry ###
class ChemistryQuestion(models.Model):
	question = models.TextField(max_length=200,default="")
	image = models.CharField(max_length=255,default="", blank = True, null = True)
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
		return reverse("chemistry:detail", kwargs={"pk" : self.pk})

class ChemistryAnswer(models.Model):	
	question = models.ForeignKey(ChemistryQuestion, on_delete = models.CASCADE, blank = False)
	solver = models.CharField(max_length = 50)

	def __str__(self):
		return "Answer by: " + self.solver + " on question " + self.question.question