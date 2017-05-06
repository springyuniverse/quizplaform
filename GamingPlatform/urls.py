from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from quiz.views import (
	register_user,
	login_user,
	logout_user
)

admin.site.site_header = 'IG Quiz administration'
admin.site.site_title = 'IG Quiz site admin'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^math/', include("quiz.MathUrls", namespace = "math")),
    url(r'^register/$', register_user, name = "register"),
    url(r'^login/$', login_user, name = "login"),
    url(r'^logout/$', logout_user, name = "logout"),
]

# Static and Media Files URLs

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)