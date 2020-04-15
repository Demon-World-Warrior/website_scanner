import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'scanme.nmap.org'
def port_scan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

for port in range(1,26):
    if port_scan(port):
        print('Port no ',port,'is open!!!')
        
    else:
        print('Port',port,'is closed')

        
