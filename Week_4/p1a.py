import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input("Enter remote host to scan: ")

def portScan(port):
    try:
        s.connect((target,port))
        return True
    except:
        return False

start = int(input('\nInput starting port number: '))
end = int(input('Input last port number: '))
flag = 0

start_time = time.time()

print("\nPort Scanning.....")
for x in range(start, end+1):
    if portScan(x):
        print('Port ',x, ' is open')
        flag =1
    else:
        print('Port ',x, ' is closed')

end_time  = time.time()

if flag==0:
    print('OOPS, no ports are open!')

print("Time elapsed: ", end_time-start_time)