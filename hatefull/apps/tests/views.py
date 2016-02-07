#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic import DetailView

from hatefull.apps.tests.models import Test


class TestDetail(DetailView):
    model = Test
    pk_url_kwarg = 'pk'
    template_name = 'test/test_detail.html'
    context_object_name = 'test'
