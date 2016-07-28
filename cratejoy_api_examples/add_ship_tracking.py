"""
This command line utility demonstrates how to add
tracking numbers to shipped shipments in Cratejoy.

This version requires reading the shipment_id, tracking_number
tuples from a csv file, which must be specified in the call.

The CSV should be of the following format:

`
headers
<shipment_id_1>, <tracking_number_1>
<shipment_id_2>, <tracking_number_2>
...
<shipment_id_3>, <tracking_number_3>
`

Example call:
  > python add_ship_tracking.py tracking_numbers.csv --user=nick --pw=password

"""

import csv
import requests
import datetime


base_url = 'http://api.cratejoy.com/v1/shipments/{}/'

shipped_at = datetime.datetime.utcnow()
shipped_at = shipped_at.strftime('%Y-%m-%d')


def put_tracking(sid, tracking_number, counter, auth, mark_shipped=False):
    """
        Add tracking number to the shipment and mark as shipped.
    """

    data = {
        'tracking_number': tracking_number,
    }

    if mark_shipped:
        data.update({
           'shipped_at': shipped_at,
           'status': 'shipped'
        })

    response = requests.put(
        base_url.format(sid),
        auth=auth,
        json=data
    )

    print(response.status_code, counter, sid)


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('filename', help='path to csv file')
    parser.add_argument(u'--user',
                        type=unicode,
                        required=True, help=u'Basic auth user')
    parser.add_argument(u'--pw',
                        type=unicode,
                        required=True, help=u'Basic auth password')

    parser.add_argument(u'--mark_shipped',
                        type=bool,
                        required=False,
                        default=False,
                        help=u'If shipments should also be marked as shipped at this time. Defaults False')

    args = parser.parse_args()

    with open(args.filename, 'rb') as btqfile:
        shipment_list = list(csv.reader(btqfile, delimiter=','))

    print "found {} shipments".format(len(shipment_list))

    auth = (args.user, args.pw)

    counter = 0
    for row in shipment_list[1:]:
        try:
            shipment_id = row[0].strip()
            tracking_number = row[1].strip()

        except (ValueError, IndexError) as e:
            print e
            continue

        put_tracking(shipment_id, tracking_number, counter, auth, args.mark_shipped)
        counter += 1
