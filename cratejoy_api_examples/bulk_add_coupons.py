"""
This command-line utility demonstrates how to bulk add
a coupon to a list of subscriptions in a text file with
the Cratejoy API.
From a high level, it's very straight-forward.
Just loop through a list of subscription ids, using a
POST request to add the coupon for each,
using the https://api.cratejoy.com/v1/subscriptions/{sub_id}/coupons/
endpoint.
Usage: python bulk_add_coupons.py --user blake --pw password --coupon_id coupon_id --subscription_ids_file /documents/file.txt
"""

import json
import requests
import time


def bulk_add_coupon(auth, file_name, coupon_id, base_url='https://api.cratejoy.com/v1/'):
    """
        Mark all of the shipment_ids as shipped
        using the Cratejoy API.
    """

    with open('{}'.format(file_name), 'r') as f:
        subscription_ids = [s.strip('\n') for s in list(f.readlines())]

    payload = json.dumps({
        u'coupon_id': coupon_id,
    })

    counter = 0

    for sub in subscription_ids:
        counter += 1
        subscription_endpoint = '{}subscriptions/{}/coupons/'.format(
            base_url, sub)
        resp = requests.post(
            subscription_endpoint,
            data=payload,
            auth=auth
        )
        print('{}) Added coupon ID {} to {}, responded with status '
              'code: {}'.format(counter, coupon_id, sub, resp.status_code))


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument(u'--user',
                        type=unicode,
                        required=True, help=u'Basic auth user')
    parser.add_argument(u'--pw',
                        type=unicode,
                        required=True, help=u'Basic auth password')
    parser.add_argument(u'--coupon_id',
                        type=int,
                        required=True, help=u'Basic auth password')
    parser.add_argument(u'--subscription_ids_file',
                        type=str,
                        required=True,
                        help=u'')
    parser.add_argument(u'--base_url',
                        type=unicode,
                        help=u'Base URL for the API (for dev only)')

    args = parser.parse_args()
    auth = (args.user, args.pw)

    fn_args = {
        'auth': auth,
        'file_name': args.subscription_ids_file,
        'coupon_id': args.coupon_id
    }

    if args.base_url:
        fn_args['base_url'] = args.base_url

    bulk_add_coupon(**fn_args)
