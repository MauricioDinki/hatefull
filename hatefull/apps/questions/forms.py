#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'question', 'correct_answer',
            'wrong_answer_1', 'wrong_answer_2', 'wrong_answer_3'
        ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(QuestionForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        question = super(QuestionForm, self).save(commit=False)
        question.user = self.request.user
        question.save()
        return question
