#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^tests/create/$', view=views.TestCreate.as_view(),
        name='test_create'),

    url(regex=r'^tests/(?P<pk>.*)/$', view=views.TestDetail.as_view(),
        name='test_detail'),
]
