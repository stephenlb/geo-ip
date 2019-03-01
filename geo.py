## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
## Import Python Libs
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import geoip2.database
import maxminddb.const
import pprint

## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
## Max Mind
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
asn = geoip2.database.Reader(
    './GeoLite2-ASN.mmdb'
,   mode=maxminddb.const.MODE_MEMORY
)
city = geoip2.database.Reader(
    './GeoLite2-City.mmdb'
,   mode=maxminddb.const.MODE_MEMORY
)

## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
## Lookup all details about IP
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def lookup(ip):
    results = { "ip" : ip }

    try:    ip_city = city.city(ip)
    except: ip_city = None
    try:    ip_asn  = asn.asn(ip)
    except: ip_asn  = None

    ## ISP
    if ip_asn:
        ## ASN Database
        results['aso'] = ip_asn.autonomous_system_organization or 'Unknown'
        results['asn'] = str(ip_asn.autonomous_system_number or 'Unknown')

    ## Location
    if ip_city:
        ## Country Database
        results['iso_code']       = str(ip_city.country.iso_code or 'Unknown')
        results['continent_code'] = str(ip_city.continent.code or 'Unknown')
        results['country']        = ip_city.country.name or 'Unknown'
        results['continent']      = ip_city.continent.name or 'Unknown'

        ## City Database
        results['zip_code']   = str(ip_city.postal.code or 'Unknown')
        results['state']      = ip_city.subdivisions.most_specific.name or 'Unknown'
        results['state_code'] = ip_city.subdivisions.most_specific.iso_code or 'Unknown'
        results['city']       = ip_city.city.name or 'Unknown'
        results['latitude']   = ip_city.location.latitude or 0.0
        results['longitude']  = ip_city.location.longitude or 0.0

    ## Dictionary with Valuable Data
    return results

## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
## Max Mind Close Databases
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def close():
    asn.close()
    city.close()
