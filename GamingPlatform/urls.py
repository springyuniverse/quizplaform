from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from quiz import views
from quiz.views import (
	register_user,
	login_user,
	logout_user,
	homepage
)

admin.site.site_header = 'IG Quiz administration'
admin.site.site_title = 'IG Quiz site admin'

router = routers.DefaultRouter()
router.register(r'math', views.MathQuestionViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage, name = "homepage"),

    url(r'^math/', include("quiz.SubjectUrls.MathUrls", namespace = "math")),
    url(r'^biology/', include("quiz.SubjectUrls.BiologyUrls", namespace = "biology")),
    url(r'^chemistry/', include("quiz.SubjectUrls.ChemistryUrls", namespace = "chemistry")),
    url(r'^physics/', include("quiz.SubjectUrls.PhysicsUrls", namespace = "physics")),
    url(r'^english/', include("quiz.SubjectUrls.EnglishUrls", namespace = "english")),

    url(r'^register/$', register_user, name = "register"),
    url(r'^login/$', login_user, name = "login"),
    url(r'^logout/$', logout_user, name = "logout"),

    url(r'^rest/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# Static and Media Files URLs

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)