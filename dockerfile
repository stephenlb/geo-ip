## Dockerfile - PubNub GEO IP Generator
FROM alpine:3.8
LABEL maintainer="Stephen Blum <stephen@pubnub.com>"

## Setup Working Directory
RUN mkdir -p /opt
WORKDIR /opt

## Install System Packages
RUN apk add --no-cache curl python2 py2-pip gzip tar
RUN pip install --upgrade pip
RUN pip install geoip2 iptools

## Download MaxMind DB
RUN curl -O http://geolite.maxmind.com/download/geoip/database/GeoLite2-ASN.tar.gz
RUN tar xvfz GeoLite2-ASN.tar.gz
RUN rm GeoLite2-ASN.tar.gz
RUN mv GeoLite2-ASN_*/GeoLite2-ASN.mmdb .
RUN rm -rf GeoLite2-ASN_*

RUN curl -O http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz
RUN tar xvfz GeoLite2-City.tar.gz
RUN rm GeoLite2-City.tar.gz
RUN mv GeoLite2-City_*/GeoLite2-City.mmdb .
RUN rm -rf GeoLite2-City_*

## Copy app files
COPY geo.py  geo.py
COPY main.py main.py
RUN chmod +x main.py

## Use SIGQUIT instead of default SIGTERM
CMD ["./main.py"]
STOPSIGNAL SIGQUIT
