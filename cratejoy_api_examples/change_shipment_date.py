"""
This command-line utility demonstrates how to change
a shipment date using the Cratejoy API.

Usage: python change_shipment_date.py --user philip --pw password --shipment_id 4124 --date 2017-06-21
"""

import json
import requests


def change_shipment_date(auth, shipment_id, date,
                    base_url='https://api.cratejoy.com/v1/'):
    """
        Change the date of the requested shipment.
    """

    payload = json.dumps({u'adjusted_ordered_at': date})

    shipment_endpoint = '{}shipments/{}/'.format(
        base_url, shipment_id)

    resp = requests.put(
        shipment_endpoint,
        data=payload,
        auth=auth
    )

    print('PUT request to {} responded with status '
          'code: {}'.format(shipment_endpoint,
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
    parser.add_argument(u'--shipment_id',
                        type=int,
                        required=True,
                        help=u'The shipment id to move')
    parser.add_argument(u'--date',
                        type=str,
                        required=True,
                        help=u'The date to set for shipment')
    parser.add_argument(u'--base_url',
                        type=unicode,
                        help=u'Base URL for the API (for dev only)')

    args = parser.parse_args()
    auth = (args.user, args.pw)

    fn_args = {
        'auth': auth,
        'shipment_id': args.shipment_id,
        'date': args.date
    }

    if args.base_url:
        fn_args['base_url'] = args.base_url

    change_shipment_date(**fn_args)
