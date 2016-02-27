#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


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

    class Meta:
        verbose_name = 'Answer'

    def __str__(self):
        return '%s %s' % (self.user.username, self.answer)


