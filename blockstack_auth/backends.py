# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from blockchainauth import AuthResponse
from jwt import DecodeError


class BlockstackAuthBackend(object):
    def authenticate(self, request, auth_response_token=None):
        try:
            verified = AuthResponse.verify(auth_response_token)
        except (ValueError, DecodeError):
            return None
        if verified:
            user, _ = User.objects.get_or_create(
                username=AuthResponse.decode(auth_response_token)['payload']['username']
            )
            return user
