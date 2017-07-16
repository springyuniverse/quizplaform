from rest_framework import serializers
from .models import *

class MathQuestionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = MathQuestion
		fields = ('question', 'option1', 'option2', 'option3', 'option4', 'answer', 'points', 'exam')