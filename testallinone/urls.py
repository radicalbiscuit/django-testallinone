from django.conf.urls import patterns, url

from hello import views as hello_views

urlpatterns = patterns('',
    url(r'^$', hello_views.HelloWorldView.as_view()),
)
