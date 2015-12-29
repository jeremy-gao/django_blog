"""website URL Configuration

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
from django.conf.urls import patterns
from blog import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', include('blog.urls')),
    url(r'^$',views.index),
    url(r'index.html$',views.index),
    url(r'^post/(?P<id>[0-9]+)/$', views.post_detail),
    url(r'^about.html$', views.about),
    url(r'^contact.html$', views.contact),
    url(r'^search', views.search),
    url(r'^page/(?P<page>\d+)/$',views.index),
    url(r'^cname/(?P<cid>\d+)/$',views.index),
    url(r'^page/(?P<page>\d+)/cname/(?P<cid>\d+)/$',views.index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)