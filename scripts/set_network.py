#!/usr/bin/env python
import sys
from itertools import izip

if __name__ == '__main__':
	args = sys.argv[2:]
	i = iter(args)
	network_settings = dict(izip(i, i))

	keys = network_settings.keys()

	err_msg = ''
	if 'ip' not in keys:
		err_msg += 'ip not specified\n'
	if 'netmask' not in keys:
		err_msg += 'netmask not specified\n'
	if 'gw' not in keys:
		err_msg += 'gw not specified\n'

	if err_msg != '':
		sys.exit()
	
	ip = network_settings['ip']
	netmask = network_settings['netmask']
	gw = network_settings['gw']

	config_file = '''
DEVICE="eth0"
BOOTPROTO="none"
ONBOOT="yes"
TYPE="Ethernet"
NETMASK="%s"
IPADDR="%s"
DNS="8.8.8.8"
GATEWAY="%s"
USERCTL="YES"
''' % (netmask, ip, gw)

	f = open('/etc/sysconfig/network-scripts/ifcfg-eth0', 'w')
	f.write(config_file)
	f.close()

	print "we should ifup eth0, but i dont want to loose access"

