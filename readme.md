# PubNub Geo IP Generator

Generates a JSON dump of IP Addresses and associated Geo information.

```shell
docker build -t geo-ip .
docker run -e IPRANGE='54.0.0.0/30' geo-ip               ## a few IPs
docker run -e IPRANGE='54.0.0.0/26' geo-ip               ## a few more IPs
docker run -e IPRANGE='54.0.0.0/16' geo-ip               ## a lot more IPs
docker run -e IPRANGE='0.0.0.0/0'   geo-ip               ## ALL IPs
docker run -e IPRANGE='0.0.0.0/0'   geo-ip > geo-ip.json ## ALL IPs saved to JSON File
docker run geo-ip 
```

This prints less than *4,228,250,625* JSON lines to STDOUT.
Here is an example of one of the lines:

```json
{"city": "Palo Alto", "ip": "0.0.0.0", "longitude": -122.1274,
 "continent": "North America", "continent_code": "NA",
 "state": "California", "country": "United States", "latitude": 37.418,
 "iso_code": "US", "state_code": "CA", "aso": "PubNub",
 "asn": "11404", "zip_code": "94107"}
```

## Private and Reserved IP Range

We automatically exclude non-usable IP addresses
following the guide from the wikipedia article:
https://en.wikipedia.org/wiki/Reserved_IP_addresses

```python
## Private IP Addresses
private = iptools.IpRangeList(
    '0.0.0.0/8',      '10.0.0.0/8',     '100.64.0.0/10', '127.0.0.0/8',
    '169.254.0.0/16', '172.16.0.0/12',  '192.0.0.0/24',  '192.0.2.0/24',
    '192.88.99.0/24', '192.168.0.0/16', '198.18.0.0/15', '198.51.100.0/24',
    '203.0.113.0/24', '224.0.0.0/4',    '240.0.0.0/4',   '255.255.255.255/32'
)
```
