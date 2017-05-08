=====
Blockstack Authentication for Django
=====

This Django application enables Blockstack-based authentication for your website.

Quick start
-----------

1. Add "django_blockstack" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_blockstack',
    ]

2. Add "django_blockstack.backends.BlockstackAuthBackend" to your AUTHENTICATION_BACKENDS setting like this::

    AUTHENTICATION_BACKENDS = [
        'django_blockstack.backends.BlockstackAuthBackend',
        ...
    ]

3. Add BLOCKSTACK_AUTH setting (blockstack_api is only needed if you run local Blockstack Core in API mode)::

    BLOCKSTACK_AUTH = {
        'settings': {
            'private_key': 'a5c61c6ca7b3e7e55edee68566aeab22e4da26baa285c7bd10e8d2218aa3b22901',
            'domain_name': 'http://localhost:8000'
        },
        'manifest': {
            'name': 'Blockstack Auth Test',
            'start_url': 'http://localhost:8000',
            'description': 'A simle demo of Blockstack Auth',
            'icons': [{
                'src': 'http://localhost:8000/static/icon.png',
                'sizes': '420x420',
                'type': 'image/png'
            }]
        },
        'blockstack_api': 'http://localhost:6270'
    }

4. Include the blockstack_auth URLconf in your project urls.py like this::

    url(r'', include('django_blockstack.urls')),

5. Redirect user to '<your_domain_name>/blockstack/request' when he tries to authenticate.

6. Get Blockstack profile of already authenticated users like this::

    >>> from blockstack_auth.profile import fetch_profile
    >>> fetch_profile(user.username)

You can see this app in action in this simple website: https://github.com/spankratov/django-blockstack-test
