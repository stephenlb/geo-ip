#!/bin/bash

## Generates a list of all valid Public Addresses
docker build -t geo-ip .
for i in $(seq 1 191);
    do docker run -e IPRANGE='$i.0.0.0/8' geo-ip >> geo-ip.json
    sleep(1)
done
