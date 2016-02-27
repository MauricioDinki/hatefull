#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic import DetailView, CreateView

from hatefull.apps.core.mixins import RequestFormMixin

from .forms import TestForm
from .models import Test


class TestDetail(DetailView):
    model = Test
    pk_url_kwarg = 'pk'
    template_name = 'tests/test_detail.html'
    context_object_name = 'test'


class TestCreate(RequestFormMixin, CreateView):
    model = Test
    template_name = 'tests/test_create.html'
    form_class = TestForm
    context_object_name = 'form'
    success_url = '/'
