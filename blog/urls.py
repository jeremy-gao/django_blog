from django.conf.urls import patterns
from django.conf.urls import url 
from django.conf.urls import include 
from blog import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$',views.index),
    url(r'^post/(?P<pk>[0-9]+)/$',views.post_detail),
]