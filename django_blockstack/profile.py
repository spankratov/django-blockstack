# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import urllib2

from django.conf import settings


BLOCKSTACK_CORE_URL = 'https://core.blockstack.org'
NAME_LOOKUP_URL = '/v2/users/'


def fetch_profile(name):
    profile = {}
    try:
        # try local blockstack api first
        blockstack_api_url = getattr(settings, 'BLOCKSTACK_AUTH', {}).get('blockstack_api', 'http://localhost:6270')
        response = urllib2.urlopen(blockstack_api_url + NAME_LOOKUP_URL + name)
        response = json.loads(response.read())
        if name in response and 'profile' in response[name]:
            profile = response[name]['profile']
    except urllib2.URLError:
        pass

    if not profile:
        try:
            # try external blockstack core api
            response = urllib2.urlopen(BLOCKSTACK_CORE_URL + NAME_LOOKUP_URL + name)
            response = json.loads(response.read())
            if name in response and 'profile' in response[name]:
                profile = response[name]['profile']
        except urllib2.URLError:
            pass

    return profile
