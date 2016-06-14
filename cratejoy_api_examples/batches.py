"""
This command-line utility demonstrates how to pull shipping batches.

Usage:
  List of batches:
      python batches.py --user luca --pw password

  Shipments by batch:
      python batches.py --user luca --pw password --batch=8675309

  Shipments by batch end date:
      python batches.py --user luca --pw password --date=2016-05-20

"""

import json
import requests
import datetime


def get_batches(auth, base_url='https://api.cratejoy.com/v1/'):
    """
        Get batches using the Cratejoy API.
    """
    
    batch_endpoint = '{}shipment_batches/'.format(base_url)

    resp = requests.get(
        batch_endpoint,
        auth=auth
    )

    print('GET request to {} responded with status '
          'code: {}'.format(batch_endpoint,
                            resp.status_code))
    print(resp.content)


def get_shipments_by_batch(auth, batch_id, base_url='https://api.cratejoy.com/v1/'):
    """
        Get shipments using the Cratejoy API.
        Only show shipments in batch [batch_id].
    """
    
    shipment_endpoint = '{}shipments/?batch_id={}'.format(base_url, batch_id)

    resp = requests.get(
        shipment_endpoint,
        auth=auth
    )

    print('GET request to {} responded with status '
          'code: {}'.format(shipment_endpoint,
                            resp.status_code))
    print(resp.content)


def get_shipments_by_date(auth, date, base_url='https://api.cratejoy.com/v1/'):
    """
        Get shipments using the Cratejoy API.
        Only show shipments in a batch that ends prior to [date].
    """
    
    shipment_endpoint = '{}shipments/?batch.end__lt={}T00:00:00Z'.format(base_url, date)

    resp = requests.get(
        shipment_endpoint,
        auth=auth
    )

    print('GET request to {} responded with status '
          'code: {}'.format(shipment_endpoint,
                            resp.status_code))
    print(resp.content)


if __name__ == '__main__':
    from argparse import ArgumentParser
    
    parser = ArgumentParser()

    parser.add_argument(u'--user',
                        type=unicode,
                        required=True, help=u'Basic auth user')
    parser.add_argument(u'--pw',
                        type=unicode,
                        required=True, help=u'Basic auth password')
    parser.add_argument(u'--base_url',
                        type=unicode,
                        help=u'Base URL for the API (for dev only)')
    parser.add_argument(u'--batch',
                        type=int,
                        required=False, help=u'Batch id')
    parser.add_argument(u'--date',
                        type=unicode,
                        required=False, help=u'Date')

    args = parser.parse_args()
    auth = (args.user, args.pw)
    
    fn_args = {
        'auth': auth,
    }

    if args.base_url:
        fn_args['base_url'] = args.base_url

    if args.batch:
        fn_args['batch_id'] = args.batch
        get_shipments_by_batch(**fn_args)
    elif args.date:
        fn_args['date'] = args.date
        get_shipments_by_date(**fn_args)
    else:
        get_batches(**fn_args)

