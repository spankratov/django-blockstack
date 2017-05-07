# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import urllib2

from django.conf import settings

from blockstack_profiles import get_token_file_url_from_zone_file


def fetch_profile(name):
    blockstack_api_url = getattr(settings, 'BLOCKSTACK_AUTH', {}).get('blockstack_api', 'http://localhost:6270')
    response = urllib2.urlopen(blockstack_api_url + '/v1/names/' + name)
    zone_file = json.loads(response.read())['zonefile']
    profile_url = get_token_file_url_from_zone_file(zone_file)
    response = urllib2.urlopen(profile_url)
    return json.loads(response.read())[0]['decodedToken']['payload']
