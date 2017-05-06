from django import forms
from .models import *

class MathQuestionForm(forms.ModelForm):
	class Meta:
		model = MathQuestion
		fields = ['option1', 'option2', 'option3', 'option4']
		widgets = {
			'option1' : forms.RadioSelect(),
			'option2' : forms.RadioSelect(),
			'option3' : forms.RadioSelect(),
			'option4' : forms.RadioSelect(),
		},
