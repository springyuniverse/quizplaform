from django.conf.urls import url
from quiz.views import (
		PhysicsDetail,
		PhysicsList,
	)

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', PhysicsDetail, name = "detail"),
    url(r'^$', PhysicsList, name = "list"),

]
