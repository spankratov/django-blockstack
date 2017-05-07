# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import urllib2

from django.conf import settings

from blockstack_profiles import get_token_file_url_from_zone_file

BLOCKSTACK_EXPLORER_URL = 'https://explorer-api.appartisan.com'


def fetch_profile(name):
    profile_url = None
    try:
        # try local blockstack api first
        blockstack_api_url = getattr(settings, 'BLOCKSTACK_AUTH', {}).get('blockstack_api', 'http://localhost:6270')
        response = urllib2.urlopen(blockstack_api_url + '/v1/names/' + name)
        zone_file = json.loads(response.read())['zonefile']
        profile_url = get_token_file_url_from_zone_file(zone_file)
    except urllib2.URLError:
        pass

    if not profile_url:
        try:
            # try external blockstack explorer
            req = urllib2.Request(BLOCKSTACK_EXPLORER_URL + '/get_name_zonefile/' + name,
                                  headers={'User-Agent': 'Magic Browser'})
            response = urllib2.urlopen(req)
            zone_file = json.loads(response.read())['zonefile']
            profile_url = zone_file['uri'][0]['target']
        except urllib2.URLError:
            pass

    if profile_url:
        try:
            response = urllib2.urlopen(profile_url)
            return json.loads(response.read())[0]['decodedToken']['payload']
        except urllib2.URLError:
            return {}
    else:
        return {}
