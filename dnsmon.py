#!/usr/bin/env python
# dnsmon.py is a simple server that provides some DNS Healthchecking for prometheus. 

import socket
import argparse
from time import sleep

import dns.resolver
from prometheus_client import start_http_server, Gauge, Counter

records = Gauge('dns_records', 'Number of DNS records associated with a domain', ['host', 'type'])
delta = Counter('dns_delta', 'Number of items that have changed in our queries', ['host', 'type']) 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('hosts', nargs='+', help="List of hosts to query")
    parser.add_argument('-s', '--sleep', help="How long to wait between updates", default=59)
    parser.add_argument('-P', '--port', help="How long to wait between updates", default=7999)

    args = parser.parse_args()

    resolver = dns.resolver.Resolver()

    lastresults = {}

    start_http_server(args.port)

    while True:
        for host in args.hosts:
            result = set(resolver.query(host))
            records.labels(host=host, type='A').set(len(result))
            if host not in lastresults:     # Initialization
                lastresults[host] = result
            delta.labels(host=host, type='A').inc(len(lastresults[host].symmetric_difference(result)))
            lastresults[host] = result
            print(result)
        sleep(args.sleep)
            


if __name__ == '__main__':
    main()
