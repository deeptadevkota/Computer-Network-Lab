import socket
import threading
from queue import Queue
import time

print_lock = threading.Lock()
target = input("\nEnter remote host to scan: ")

def portScan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection = s.connect((target,port))
        with print_lock:
            print('Port ', port, ' is open!')
        connection.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        portScan(worker)
        q.task_done()
q = Queue()
for x in range(30):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()
start = int(input('\nInput starting port number: '))
end = int(input('Input last port number: '))
start_time = time.time()
print("\nPort Scanning.....")
for worker in range(start,end+1):
    q.put(worker)
q.join()
end_time  = time.time()
print("\nTime elapsed: ", end_time-start_time, '\n')