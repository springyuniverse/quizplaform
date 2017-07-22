from django.conf.urls import url
from quiz.views import (
		ChemistryDetail,
		ChemistryListView
	)

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ChemistryDetail, name = "detail"),
    url(r'^$', ChemistryListView.as_view(), name = "list"),

]
