#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models

from hatefull.apps.questions.models import Question


class Test(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='User',
        blank=False,
        null=False,
    )
    name = models.CharField(
        blank=False,
        null=False,
        max_length=20
    )
    questions = models.ManyToManyField(Question)

    def __unicode__(self):
        return self.name
