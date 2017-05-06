# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.urls import reverse

from blockchainauth import AuthRequest


def blockstack_request(request):
    blockstack_auth_settings = settings.BLOCKSTACK_AUTH['settings']
    blockstack_auth_settings['private_key'] = blockstack_auth_settings.get('private_key', None)
    blockstack_auth_settings['manifest_uri'] = blockstack_auth_settings['domain_name'] + reverse('blockstack:manifest')
    blockstack_auth_settings['redirect_uri'] = blockstack_auth_settings['domain_name'] + reverse('blockstack:response')
    ar = AuthRequest(**blockstack_auth_settings)
    if not AuthRequest.verify(ar.token()):
        return HttpResponse('Can\'t generate Blockstack authentication request token', status=500)
    else:
        response = HttpResponse("", status=302)
        response['Location'] = ar.redirect_url()
        return response


def blockstack_response(request):
    auth_response_token = request.GET.get('authResponse')
    if not auth_response_token:
        return HttpResponseBadRequest('No authResponse parameter')
    user = authenticate(request, auth_response_token=auth_response_token)
    if user is not None:
        login(request, user)
    response = HttpResponse("", status=302)
    response['Location'] = '{scheme}://{host}'.format(scheme=request.scheme,
                                                      host=request.get_host())
    return response


def manifest(request):
    result = JsonResponse(settings.BLOCKSTACK_AUTH['manifest'])
    result['Access-Control-Allow-Origin'] = '*'
    return result
