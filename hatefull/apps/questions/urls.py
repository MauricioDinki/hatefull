#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^questions/create/$', view=views.CreateQuestion.as_view(),
        name='question_create'),
]
