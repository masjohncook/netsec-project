import sys
from modules.scanning import Scanner
# from modules.gain_access import gain_access

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
        scan.ping_target()
        scan.check_status()
        scan.scanning_target()
        pass
    except Exception as e:
        print(e)
        pass


main(sys.argv)