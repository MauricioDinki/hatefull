#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Test


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('user', 'name',)
