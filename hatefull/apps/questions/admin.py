#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'question')
    list_filter = ('user',)
