from django.conf.urls import url
from quiz.views import (
		PhysicsDetail,
		PhysicsListView
	)

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', PhysicsDetail, name = "detail"),
    url(r'^$', PhysicsListView.as_view(), name = "list"),

]
