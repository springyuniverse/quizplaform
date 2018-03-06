from django.conf.urls import url
from quiz.views import (
		MathTopicDetail,
		MathSetDetail,
		MathList,
		MathQuestionDetail
	)


urlpatterns = [
    # url(r'^(?P<pk>\d+)/$', MathDetail, name = "topic"),
    url(r'^$', MathList), # Displays all topics
    url(r'^(?P<slug>[\w-]+)/$', MathTopicDetail, name='topic'), # Displays all sets
    url(r'^(?P<topic>[\w-]+)/(?P<pk>\d+)/$', MathSetDetail, name='set'), # Displays all questions
    url(r'^(?P<topic>[\w-]+)/(?P<pk>\d+)/(?P<id>\d+)/$', MathQuestionDetail, name='detail'), # Displays question
]