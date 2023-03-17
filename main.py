import subprocess as sub
import re
import time


time.sleep(1)
interface = ("[+] Enter interface name: ")
new_mac = ("[+] Enter new MAC: ")

def change_mac(interface, new_mac):

  if len(new_mac) != 17:
    print('[-] Please enter valid MAC Address')
    quit()
  
  print('\n[+] Changing the MAC Address to', new_mac)
  sub.call(['sudo', 'ifconfig', interface, 'down'])
  sub.call(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])
  sub.call(['sudo', 'ifconfig', interface, 'up'])
  
def get_current_mac(interface):
  output = sub.check_output(['ifconfig', interface], universal_newlines = True)
  search_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output)
  if search_mac:
    return search_mac.group(0)
  else:
    print('[-] Could not read the MAC Address')
    
prev_mac = get_current_mac(interface)
print('\n[+] MAC Address before changing -> {}'.format(prev_mac))

change_mac(interface, new_mac)

changed_mac = get_current_mac(interface)
print('\n[+] MAC Address after change -> {}'.format(changed_mac))

if changed_mac == new_mac:
  print('\n[+] MAC Address was successfully changed from {} to {}'.format(prev_mac, changed_mac))
else:
  print('\n[-] Could not change the MAC Address')
time.sleep(10)