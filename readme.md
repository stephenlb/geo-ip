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
{"city": "Palo Alto", "ip": "0.0.0.0", "longitude": -122.1274, "continent": "North America", "continent_code": "NA", "state": "California", "country": "United States", "latitude": 37.418, "iso_code": "US", "state_code": "CA", "aso": "PubNub", "asn": "11404", "zip_code": "94107"}
```
