"""
This command-line utility demonstrates how to mark 
a shipment or group of shipments as shipped with 
the Cratejoy API.

From a high level, it's very straight-forward. 
Just loop through a list of shipment ids, using a 
PUT request to update the "status" field for each, 
using the http://api.cratejoy.com/v1/shipments/<shipment_id> 
endpoint.

Usage: python mark_as_shipped.py --user blake --pw password --shipment_id 4124

"""

import json
import requests


def mark_as_shipped(auth, shipment_id,
                    base_url='http://api.cratejoy.com/v1/'):
    """
        Mark all of the shipment_ids as shipped
        using the Cratejoy API.
    """
    
    payload = json.dumps({u'status': u'shipped'})

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
                        help=u'The shipment id to mark as shipped')
    parser.add_argument(u'--base_url',
                        type=unicode,
                        help=u'Base URL for the API (for dev only)')

    args = parser.parse_args()
    auth = (args.user, args.pw)
    
    fn_args = {
        'auth': auth,
        'shipment_id': args.shipment_id,
    }

    if args.base_url:
        fn_args['base_url'] = args.base_url

    mark_as_shipped(**fn_args)

