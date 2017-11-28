from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from indie_network.authentication.views import IndexView, HomeView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^home', HomeView.as_view(), name='home')
]
