#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Flynn on 2018-02-25 15:09
from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
	url(r'^$', views.get_blogs, name='index'),
	url(r'^detail/(?P<pk>\d+)$', views.get_detail, name='detail'),
]
