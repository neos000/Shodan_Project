#!/usr/bin/env python
# Dependencies.
# This script was created by PotOfGreed. It is still in need of changes.
import shodan 
import time
import sys
import time

# Main function
def main():
    api = shodan.Shodan(sys.argv[1])
    
    print('[---] Script created by neos [---]\n[---] Grabbing data...[---]\n')
    
    server_list = [
            'mysql', 'nginx', 'redis',
            ]
     
    element_filters = [
              'org', 'product', 'ip_str', 
              'port', 'hostnames',
            ]
            
    for srvs in server_list:
        try:
            results = api.search(srvs)
            time.sleep(2)
            for result in results['matches']:
                for elements in element_filters:
                    time.sleep(2)                        
                    print('[*] %s: %a' % (elements, result[elements]))
                print('\n')
        except:
            print('[*] Error occured...\n')




# Conditional statement: Function call
if __name__ == '__main__':
    main()
