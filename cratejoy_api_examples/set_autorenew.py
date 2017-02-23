"""
This command-line utility demonstrates how to switch a gift subscription from
non-autorenewing to autonewing.

Gifitng 3.0 gives the option to have subscriptions autorenew or not, but
subscribers aren't able to change it after the fact. This script will allow
the merchant to flip it for them.

Usage:
python set_autorenew.py --user blake --pw secret123 --subscription 4124 --autorenew=True
python set_autorenew.py --user blake --pw secret123 --subscription 4124 --autorenew=False

"""

import json
import requests


def set_autorenew(auth, subscription_id, autorenew,
                    base_url='https://api.cratejoy.com/v1/'):
    
    payload = json.dumps({u'autorenew': u'{}'.format(autorenew)})

    subscription_endpoint = '{}subscriptions/{}/'.format(
        base_url, subscription_id)

    resp = requests.put(
        subscription_endpoint,
        data=payload,
        auth=auth
    )

    print('PUT request to {} ({}) responded with status '
          'code: {}'.format(subscription_endpoint,
                            payload,
                            resp.status_code))


if __name__ == '__main__':
    from argparse import ArgumentParser
    
    parser = ArgumentParser()

    parser.add_argument(u'--user',
                        type=unicode,
                        required=True, help=u'Basic auth user')
    parser.add_argument(u'--pw',
                        type=unicode,
                        required=True, help=u'Basic auth password')
    parser.add_argument(u'--subscription',
                        type=int,
                        required=True,
                        help=u'The subscription to modify')
    parser.add_argument(u'--autorenew',
                        type=lambda s: s.lower() in ['true', 't', '1'],
                        required=True,
                        help=u'How to set the subscription. (Defaults to false)')
    parser.add_argument(u'--base_url',
                        type=unicode,
                        help=u'Base URL for the API (for dev only)')

    args = parser.parse_args()
    auth = (args.user, args.pw)
    
    fn_args = {
        'auth': auth,
        'subscription_id': args.subscription,
        'autorenew': args.autorenew,
    }

    if args.base_url:
        fn_args['base_url'] = args.base_url

    set_autorenew(**fn_args)
