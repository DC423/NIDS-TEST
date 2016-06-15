#!/usr/bin/env python
#
# Author: @tothehilt
# DC423 Project to test an NIDS if its working
# Based off a snort rule located:
# https://github.com/DC423/NIDS-TEST/blob/master/nids-test.rules
#
#########################################
import socket
import sys

# Argument Checking
if (len(sys.argv) != 2): 
	print("USAGE: Python ./NIDS-TEST.py <host>")
	sys.exit()

# host is passed in via cli arguments
host=sys.argv[1]
# LTS port
port=1337
# Messages defined by IDS rules
MESSAGE1 = "NIDS-TEST-PACKET-LOW"
MESSAGE2 = "NIDS-TEST-PACKET-MED"
MESSAGE3 = "NIDS-TEST-PACKET-HIGH"
# create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# send all three messages
sock.sendto(MESSAGE1, (host, port))
sock.sendto(MESSAGE2, (host, port))
sock.sendto(MESSAGE3, (host, port))
# close the socket, just incase you didn't get reset by peer..
sock.close()
