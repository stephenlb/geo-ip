#!/usr/bin/python

## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
## Import Python Libs
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import os
import geo
import iptools
import json

## Get IP Range
IPRANGE = os.environ.get( 'IPRANGE', '52.0.0.0/30' )

## Private IP Addresses
private = iptools.IpRangeList(
    '0.0.0.0/8',      '10.0.0.0/8',     '100.64.0.0/10', '127.0.0.0/8',
    '169.254.0.0/16', '172.16.0.0/12',  '192.0.0.0/24',  '192.0.2.0/24',
    '192.88.99.0/24', '192.168.0.0/16', '198.18.0.0/15', '198.51.100.0/24',
    '203.0.113.0/24', '224.0.0.0/4',    '240.0.0.0/4',   '255.255.255.255/32'
)

## Find Valid Public IPs
for ip in iptools.IpRange(IPRANGE):
    if ip not in private:
        print json.dumps(geo.lookup(ip))

