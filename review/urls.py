from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

# from . import views

urlpatterns = [
	url(r'^$', RedirectView.as_view(url='/review', permanent=True), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^review/', include('webview.urls')),
]
