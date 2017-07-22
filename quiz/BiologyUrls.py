from django.conf.urls import url
from quiz.views import (
		BiologyDetail,
		BiologyListView
	)

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BiologyDetail, name = "detail"),
    url(r'^$', BiologyListView.as_view(), name = "list"),

]
