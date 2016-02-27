#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from hatefull.apps.questions.models import Question

from .models import Test


class TestForm(forms.ModelForm):

    class Meta:
        model = Test
        fields = [
            'name', 'questions'
        ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(TestForm, self).__init__(*args, **kwargs)
        self.fields['questions'] = forms.ModelMultipleChoiceField(
            queryset=Question.objects.filter(
                user=self.request.user,
            ),
            widget=forms.CheckboxSelectMultiple()
        )

    def save(self, *args, **kwargs):
        test = super(TestForm, self).save(commit=False)
        test.user = self.request.user
        test.save()
        self.save_m2m()
        return test
