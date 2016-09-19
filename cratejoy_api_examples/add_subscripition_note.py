"""
This command-line utility demonstrates how to add a subscription note.

Usage: python ./add_subscripition_note.py --id=12345678 --note="This subscription is noteworthy." --user=luca --pw=password

Note: This will overwrite any existing subscription note.
"""

import json
import requests


def add_note(auth, id, note, base_url='https://api.cratejoy.com/v1/'):
    
    payload = json.dumps({u'note': note})

    endpoint = '{}subscriptions/{}/'.format(base_url, id)

    resp = requests.put(
        endpoint,
        data=payload,
        auth=auth
    )

    print('PUT request to {} responded with status '
          'code: {}'.format(endpoint,
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
    parser.add_argument(u'--id',
                        type=int,
                        required=True,
                        help=u'The subscription id')
    parser.add_argument(u'--note',
                        type=str,
                        required=True,
                        help=u'The note to add.')
    parser.add_argument(u'--base_url',
                        type=unicode,
                        help=u'Base URL for the API (for dev only)')

    args = parser.parse_args()
    auth = (args.user, args.pw)
    
    fn_args = {
        'auth': auth,
        'id': args.id,
        'note': args.note
    }

    if args.base_url:
        fn_args['base_url'] = args.base_url

    add_note(**fn_args)

