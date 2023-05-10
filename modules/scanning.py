import nmap
from ping3 import ping, verbose_ping


class Scanner():
    
    
    def __init__(self, target_ip, target_port):
        self.ip = target_ip
        self.port = target_port
        
    # perform ping to the target to check simulate the host ping
    def ping_target(self):
        print(verbose_ping(self.ip, count=20))
        
    # check the host status through nmap
    def check_status(self):
        nm = nmap.PortScanner()
        status = nm.scan(hosts=self.ip, arguments='-n -sP -PE -PA21,23,80,3389')
        host_status = nm[self.ip]['status']['state']
        print("Target {} is {}".format(self.ip, host_status))
    
    # perform full open scan using Nmap
    def scanning_target(self):
        nm = nmap.PortScanner()
        result = nm.scan(hosts=self.ip, arguments='-O -A -p 0-65535')
        