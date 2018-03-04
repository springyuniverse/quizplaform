from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from quiz import views
from quiz.views import (
	register_user,
	login_user,
	logout_user,
	homepage
)

admin.site.site_header = 'IG Quiz administration'
admin.site.site_title = 'IG Quiz site admin'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage, name = "homepage"),

    url(r'^math/', include("quiz.MathUrls", namespace = "math")),
    url(r'^biology/', include("quiz.BiologyUrls", namespace = "biology")),
    url(r'^chemistry/', include("quiz.ChemistryUrls", namespace = "chemistry")),
    url(r'^physics/', include("quiz.PhysicsUrls", namespace = "physics")),
    url(r'^english/', include("quiz.EnglishUrls", namespace = "english")),

    url(r'^register/$', register_user, name = "register"),
    url(r'^login/$', login_user, name = "login"),
    url(r'^logout/$', logout_user, name = "logout"),
]

# Static and Media Files URLs

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)