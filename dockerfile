# Dockerfile - PubNub GEO IP Generator
FROM alpine:3.8
LABEL maintainer="Stephen Blum <stephen@pubnub.com>"

## Install System Packages
RUN apk add --no-cache curl python2 py2-pip gzip
RUN pip install --upgrade pip
RUN pip install geoip2

## Download MaxMind DB
WORKDIR /opt
RUN curl -O http://geolite.maxmind.com/download/geoip/database/GeoLite2-ASN.mmdb.gz
RUN curl -O http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz
RUN gunzip GeoLite2-ASN.mmdb.gz
RUN gunzip GeoLite2-City.mmdb.gz

# Copy app files
COPY geo.py  /opt/geo.py
COPY main.py /opt/main.py

CMD ["python main.py"]

# Use SIGQUIT instead of default SIGTERM
STOPSIGNAL SIGQUIT
