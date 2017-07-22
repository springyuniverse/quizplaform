from django.conf.urls import url
from quiz.views import (
		EnglishDetail,
		EnglishListView
	)

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', EnglishDetail, name = "detail"),
    url(r'^$', EnglishListView.as_view(), name = "list"),

]
