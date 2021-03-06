"""siblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from homepage import views as homepage_views
from post import views as post_views
#from tinymce import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage_views.index),
    url(r'^posts/', post_views.posts),
    url(r'^post/(\d+)', post_views.detail_post),
    url(r'^page/(\d+)', post_views.statis),
    url(r'^category/(\d+)', post_views.categories),
    #url(r'^upload/', post_views.simple_upload),
]
