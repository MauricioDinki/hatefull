#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import TemplateView

from hatefull.apps.core.mixins import AuthRedirectMixin


class LoginView(AuthRedirectMixin, TemplateView):
    template_name = 'xauth/login.html'


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('/')
