#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='User',
        blank=False,
        null=False,
    )
    question = models.CharField(
        blank=False,
        null=False,
        max_length=50,
    )
    correct_answer = models.CharField(
        blank=False,
        null=False,
        max_length=50,
    )
    wrong_answer_1 = models.CharField(
        blank=False,
        null=False,
        max_length=50,
    )
    wrong_answer_2 = models.CharField(
        blank=False,
        null=False,
        max_length=50,
    )
    wrong_answer_3 = models.CharField(
        blank=False,
        null=False,
        max_length=50,
    )

    def __unicode__(self):
        return self.question
