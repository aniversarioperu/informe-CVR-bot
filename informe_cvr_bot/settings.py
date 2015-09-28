import json
import os
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRETS_FILE = os.path.join(BASE_DIR, 'config.json')

if os.path.isfile(SECRETS_FILE):
    with open(SECRETS_FILE) as f:
        secrets = json.loads(f.read())
else:
    secrets = {
        'twitter_key': '',
        'twitter_secret': '',
        'twitter_token': '',
        'twitter_token_secret': '',
        'bitly_token': '',
    }


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        print(error_msg)
        sys.exit()

key = get_secret('twitter_key')
secret = get_secret('twitter_secret')
token = get_secret('twitter_token')
token_secret = get_secret('twitter_token_secret')
bitly_token = get_secret('bitly_token')
