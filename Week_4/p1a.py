import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = input("Enter remote host to scan: ")

def portScan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

start = input('\nInput starting port number: ')
end = input('Input last port number: ')
flag = 0

for x in range(start, end+1):
    if portScan(x):
        print('Port ',x, ' is open')
        flag =1
    else:
        pass

if flag==0:
    print('OOPS, no ports are open!')