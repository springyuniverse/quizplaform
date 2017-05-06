from django.conf.urls import url
from django.contrib import admin

from quiz.views import (
		MathDetail,
		MathListView
	)

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', MathDetail, name = "detail"),
    url(r'^$', MathListView.as_view(), name = "list"),

]
