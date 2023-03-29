#!/usr/bin/env python
# Dependencies - Shodan
import shodan 
import time

# Main class
class Shodan:
    def __init__(self, key):
        self.key = key

    def scan_server(self, server):
        api = shodan.Shodan(self.key)
        results = api.search(server)
        for result in results['matches']:
            print('[*] Organization: %s' % (result['org']))
            print('[*] SERVER: %s' % (result['product']))
            print('[*] IPv4: %s' % (result['ip_str']))
            print('[*] HOSTNAMES: %s' % (result['hostnames']))
            print('[*] OS: %s' % (result['os']))
            print('')
            time.sleep(0.05)
            
    def host_lookup(self, ip):
        api = shodan.Shodan(self.key)
        results = api.host(ip)
        print('I am still working on this...')
        
