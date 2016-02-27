#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import redirect


class AuthRedirectMixin(object):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('/')
        else:
            return super(AuthRedirectMixin, self).get(self, request, *args,
                                                      **kwargs)


class RequestFormMixin(object):
    def get_form_kwargs(self):
        kwargs = super(RequestFormMixin, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
