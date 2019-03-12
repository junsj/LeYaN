"""ufo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import website.views

urlpatterns = [
    url(r'crawlers/$',website.views.crawlers),
    url(r'new/$',website.views.new),
##    url(r'movies/(?P<category_mv>.*)/.*',yun.views.movies),
##    url(r'miniav/(?P<category_av>.*)/(?P<date_av>.*)/(?P<page_av>.*)/$',yun.views.miniav),
##    url(r'miniav/(?P<category_av>.*)/(?P<date_av>.*)/$',yun.views.miniav),
##    url(r'miniav/(?P<category_av>.*)/.*',yun.views.miniav_redirect),
##    url(r'miniav/.*',yun.views.miniav),
##    url(r'miniimg/list/(\d+)/$',yun.views.miniimg),
##    url(r'miniimg/(?P<movies_id>.*)/$',yun.views.miniimg_show),
##    url(r'miniimg/$',yun.views.miniimg),
    url(r'.*',website.views.home),
]
