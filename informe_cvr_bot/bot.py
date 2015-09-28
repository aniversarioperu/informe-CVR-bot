import json
import os
import requests

from .oauth_api import get_oauth
from .settings import BASE_DIR


LAST_TWEETED_FILE = os.path.join(BASE_DIR, 'last_tweeted.txt')

def send_tweet(item):
    oauth = get_oauth()
    status = item['sentence']
    payload = {
        'status': status,
    }
    url = 'https://api.twitter.com/1.1/statuses/update.json'
    res = requests.post(url=url, auth=oauth, params=payload)

    print("Tweeting: {0} {1}".format(item['index'], status))
    res_json = res.json()
    if 'errors' in res_json:
        print(res_json)
    else:
        with open(LAST_TWEETED_FILE, 'w') as handle:
            handle.write(str(item['index']) + '\n')


def tweet():
    if not os.path.isfile(LAST_TWEETED_FILE):
        last_twetted = -1
    else:
        with open(LAST_TWEETED_FILE, "r") as handle:
            last_twetted = handle.read().strip()
            if last_twetted:
                last_twetted = int(last_twetted)
            else:
                last_twetted = 0

    with open(os.path.join(BASE_DIR, 'data.json'), 'r') as handle:
        data = json.loads(handle.read())

    for item in data:
        if int(item['index']) > int(last_twetted):
            send_tweet(item)
            break


def main():
    tweet()


if __name__ == '__main__':
    main()
