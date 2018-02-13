"""
This command-line utility demonstrates how to change
a subscription renewal date using the Cratejoy API.

Usage: python change_renewal_date.py --user philip --pw password --subscription_id 4124 --date 2018-02-13
"""

import json
import requests


def change_renewal_date(auth, subscription_id, date,
                    base_url='https://api.cratejoy.com/v1/'):
    """
        Change the renewal date of the requested subscription.
    """

    payload = json.dumps({u'end_date': date})

    subscriptions_endpoint = '{}subscriptions/{}/'.format(
        base_url, subscription_id)

    resp = requests.put(
        subscriptions_endpoint,
        data=payload,
        auth=auth
    )

    print('PUT request to {} responded with status '
          'code: {}'.format(subscriptions_endpoint,
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
    parser.add_argument(u'--subscription_id',
                        type=int,
                        required=True,
                        help=u'The subscription id to move')
    parser.add_argument(u'--date',
                        type=str,
                        required=True,
                        help=u'The date to set for subscription')
    parser.add_argument(u'--base_url',
                        type=unicode,
                        help=u'Base URL for the API (for dev only)')

    args = parser.parse_args()
    auth = (args.user, args.pw)

    fn_args = {
        'auth': auth,
        'subscription_id': args.subscription_id,
        'date': args.date
    }

    if args.base_url:
        fn_args['base_url'] = args.base_url

    change_renewal_date(**fn_args)
