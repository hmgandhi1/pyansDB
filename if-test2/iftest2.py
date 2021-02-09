#!/usr/bin/env python3
# ipchk = '192.168.0.1'
ipchk = input('Apply an IP address: ') # this line now prompts the user for input

if ipchk: # if any data is provided, this will test true
   print('Looks like the IP address was set: ' + ipchk) # indented under if
else: # if data is NOT provided
   print('You did not provide input.') # indented under else

if ipchk == '1.1.1.1': # if a match on '1.1.1.1'
   # indented under if
   print('Looks like the IP address of the Gateway was set: ' + ipchk + ' This is not recommended.')
elif ipchk: # if any data is provided, this will test true
   print('Looks like the IP address was set: ' + ipchk) # indented under if
else: # if data is NOT provided
   print('You did not provide input.') # indented under else



