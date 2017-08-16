from django.conf.urls import url
from quiz.views import (
		ChemistryDetail,
		ChemistryList,
	)

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ChemistryDetail, name = "detail"),
    url(r'^$', ChemistryList, name = "list"),

]
