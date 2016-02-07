#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

from hatefull.apps.questions.models import Question
from hatefull.apps.tests.models import Test


class Answer(models.Model):

    user = models.ForeignKey(
        User,
        verbose_name='User',
        related_name="user",
        blank=False,
        null=False
    )

    answer = models.CharField(
        blank=False,
        null=False,
        max_length=50,
    )

    question = models.ForeignKey(
        Question,
        verbose_name='Question',
        blank=False,
        null=False
    )

    question_owner = models.ForeignKey(
        User,
        verbose_name='Question owner',
        related_name="owner",
        blank=False,
        null=False,
    )

    test = models.ForeignKey(
        Test,
        verbose_name='Test',
        blank=False,
        null=False,
    )

