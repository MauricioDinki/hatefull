#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^test/(?P<pk>.*)/$', view=views.TestDetail.as_view(),
        name='test_detail'),
]
