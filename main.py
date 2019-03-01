## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
## Import Python Libs
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import geo
import json

for one in xrange(0,255):
    for two in xrange(0,255):
        for three in xrange(0,255):
            for four in xrange(0,255):
                result = geo.lookup(".".join([one,two,three,four]))
                if result.get('country') == 'Unknown':
                    print json.dumps(result)
