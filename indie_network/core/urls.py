from django.conf.urls import url, include

#from . import views

urlpatterns = [
    #url(r'^', views.index),
    url(r'^', include('social_django.urls', namespace='social')),
    url(r'^', include('indie_network.authentication.urls', namespace='auth')),
]
