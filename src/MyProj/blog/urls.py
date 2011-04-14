from django.conf.urls.defaults import *
from MyProj.blog.views import archive
from django.conf.project_template.urls import urlpatterns

urlpatterns=patterns('',
    url(r'^$',archive),                     
)