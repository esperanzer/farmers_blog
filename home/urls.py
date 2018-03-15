from __future__ import absolute_import
from . views import HomeView
from django.conf.urls import url


urlpatterns = [
	url(r'^$', HomeView.as_view()),

]
