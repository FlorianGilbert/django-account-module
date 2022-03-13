# Account Django Module

The purpose of this module is to avoid having to rewrite a 
connection module everytime.
This module takes care of all the connection system.

Don't forget to add this in `settings.py`
```python
# Account APP
LOGIN_REDIRECT_URL = 'account:dashboard'
LOGIN_URL = 'account:login'
LOGOUT_URL = 'account:logout'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
]
```

And add the `account` module at the top of the `INSTALLED_APPS` in `settings.py`
