# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from django_blockstack import views

app_name = 'blockstack'

urlpatterns = [
    url(r'^blockstack/request', views.blockstack_request, name='request'),
    url(r'^blockstack/response', views.blockstack_response, name='response'),
    url(r'^blockstack/manifest.json', views.manifest, name='manifest')
]
