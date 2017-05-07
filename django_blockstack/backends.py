# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from blockchainauth import AuthResponse
from jwt import DecodeError

from django_blockstack.profile import fetch_profile


class BlockstackAuthBackend(object):
    def authenticate(self, request, auth_response_token=None):
        try:
            verified = AuthResponse.verify(auth_response_token)
        except (ValueError, DecodeError):
            return None
        if verified:
            username = AuthResponse.decode(auth_response_token)['payload']['username']
            user, _ = User.objects.get_or_create(
                username=username
            )
            try:
                profile = fetch_profile(username)
            except:
                pass
            else:
                claim = profile.get('claim', {})
                name = claim.get('name', None)
                if name:
                    name = name.split(' ', 1)
                    user.first_name = name[0]
                    if len(name) == 2:
                        user.last_name = name[1]
                    user.save()
            return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
