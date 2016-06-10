"""
This command-line utility demonstrates how to add a basic 301 or 302 redirect
to your store.


From a high level, it's very straight-forward. 
Just loop through a list of shipment ids, using a 
PUT request to update the "status" field for each, 
using the http://api.cratejoy.com/v1/shipments/<shipment_id> 
endpoint.

Usage: python add_redirect.py --user luca --pw password --redirect_type 301 --origin /fun --target /work

"""

import json
import requests


def add_redirect(auth, origin, target, redirect_type=302,
                    base_url='https://api.cratejoy.com/v1/'):
    """
        Redirect [your store domain]/fun to [your store domain]/work
        using the Cratejoy API.
    """
    
    payload = json.dumps({\
        u'path': origin,\
        u'target': target,\
        u'enabled': True,\
        u'code': redirect_type
    })

    redirect_endpoint = '{}page_redirects/'.format(base_url)

    resp = requests.post(
        redirect_endpoint,
        data=payload,
        auth=auth
    )

    print('PUT request to {} responded with status '
          'code: {}'.format(redirect_endpoint,
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
    parser.add_argument(u'--redirect_type',
                        type=int,
                        required=True,
                        help=u'The http redirect code. Either 301 (permanent\
                                redirect) or 302 (temporary redirect)')
    parser.add_argument(u'--origin',
                        type=str,
                        required=True,
                        help=u'The path to redirect from. Example: "/oldurl"')
    parser.add_argument(u'--target',
                        type=str,
                        required=True,
                        help=u'The path to redirect to. Example: "/newurl"')
    parser.add_argument(u'--base_url',
                        type=unicode,
                        help=u'Base URL for the API (for dev only)')

    args = parser.parse_args()
    auth = (args.user, args.pw)
    
    fn_args = {
        'auth': auth,
        'redirect_type': args.redirect_type,
        'origin': args.origin,
        'target': args.target
    }

    if args.base_url:
        fn_args['base_url'] = args.base_url

    add_redirect(**fn_args)

