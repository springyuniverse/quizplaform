from django.conf.urls import url
from quiz.views import (
		MathDetail,
		MathList,
	)

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', MathDetail, name = "detail"),
    url(r'^$', MathList, name = "list"),
]
