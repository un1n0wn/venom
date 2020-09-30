#!/bin/python3

def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())

import os
from subprocess import Popen
import sys
from datetime import datetime
import socket
from scapy.all import ARP, Ether, srp

os.system('cls' if os.name == 'nt' else 'clear')


logo = ''' 
 ██▒   █▓▓█████  ███▄    █  ▒█████   ███▄ ▄███▓
▓██░   █▒▓█   ▀  ██ ▀█   █ ▒██▒  ██▒▓██▒▀█▀ ██▒
 ▓██  █▒░▒███   ▓██  ▀█ ██▒▒██░  ██▒▓██    ▓██░
  ▒██ █░░▒▓█  ▄ ▓██▒  ▐▌██▒▒██   ██░▒██    ▒██ 
   ▒▀█░  ░▒████▒▒██░   ▓██░░ ████▓▒░▒██▒   ░██▒
   ░ ▐░  ░░ ▒░ ░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░
   ░ ░░   ░ ░  ░░ ░░   ░ ▒░  ░ ▒ ▒░ ░  ░      ░
     ░░     ░      ░   ░ ░ ░ ░ ░ ▒  ░      ░   
      ░     ░  ░         ░     ░ ░         ░   
     ░                                         
                                               
                                                                                              
(1) port scanner                                               
(2) password-generator                                               
(3) payload-generator                                               
(4) ddos tool                                               
(5) phishing tool                                               
                                               
          
        (x) quit
                
                    
'''

print(logo)

choice = input('option: ')

if choice == "1":
     os.system('cls' if os.name == 'nt' else 'clear')
     run("/usr/bin/scanner.py")
elif choice == "2":
     os.system('cls' if os.name == 'nt' else 'clear')
     run("/usr/bin/passwd.py")
elif choice == "3":
     os.system('cls' if os.name == 'nt' else 'clear')
     run("/usr/bin/payload.py")
elif choice == "4":
     os.system('cls' if os.name == 'nt' else 'clear')
     run('/usr/bin/ddos.py')
elif choice == "5":
     os.system('cls' if os.name == 'nt' else 'clear')
     os.system('sh phish.py')
elif choice == "x":
     os.system('cls' if os.name == 'nt' else 'clear')
     quit()

