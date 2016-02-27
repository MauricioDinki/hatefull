#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic import CreateView

from hatefull.apps.core.mixins import RequestFormMixin
from hatefull.apps.questions.forms import QuestionForm
from hatefull.apps.questions.models import Question


class CreateQuestion(RequestFormMixin, CreateView):
    form_class = QuestionForm
    template_name = 'questions/question_create.html'
    context_object_name = 'form'
    success_url = '/questions/create/'


