#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from hatefull.apps.answers.models import Answer


class Question(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='User',
        blank=False,
        null=False,
    )
    question = models.CharField(
        verbose_name='Question',
        blank=False,
        null=False,
        max_length=50,
    )
    correct_answer = models.CharField(
        verbose_name='Correct answer',
        blank=False,
        null=False,
        max_length=50,
    )
    wrong_answer_1 = models.CharField(
        verbose_name='Wrong answer 1',
        blank=False,
        null=False,
        max_length=50,
    )
    wrong_answer_2 = models.CharField(
        verbose_name='Wrong answer 2',
        blank=False,
        null=False,
        max_length=50,
    )
    wrong_answer_3 = models.CharField(
        verbose_name='Wrong answer 3',
        blank=False,
        null=False,
        max_length=50,
    )

    answers = models.ManyToManyField(
        Answer,
        related_name='answers',
        verbose_name='Answers',
        blank=True,

    )

    def __str__(self):
        return self.question
