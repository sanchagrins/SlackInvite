# ----------------------
# Configuration file for the Django-SlackInvite App. Set your community name and
# slack url here.
# ----------------------

import os
from django.core.exceptions import ImproperlyConfigured

# SECURITY WARNING: Keep you slack token private in production
def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)

slack_token = get_env_variable('SLACK_TOKEN')

# Set your community name and slack_url below
community = 'Team-Name'
slack_url = 'django-slackinvite.slack.com'
