from django.conf.urls import url
from quiz.views import (
		BiologyDetail,
		BiologyList,
	)

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BiologyDetail, name = "detail"),
    url(r'^$', BiologyList, name = "list"),

]
