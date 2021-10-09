import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = input("Enter website or IP address to scan: ")

def portScan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

for x in range(1,100):
    if portScan(x):
        print('Port ',x, ' is open')
    else:
        print('Port ', x, ' is close')