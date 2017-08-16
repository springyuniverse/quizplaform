from django.conf.urls import url
from quiz.views import (
		EnglishDetail,
		EnglishList,
	)

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', EnglishDetail, name = "detail"),
    url(r'^$', EnglishList, name = "list"),

]
