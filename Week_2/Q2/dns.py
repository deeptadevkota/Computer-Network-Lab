import socket

# function get host id from host name
def get_HOST_Name_from_IP_Address(hostName):
    try:
        host_IP = socket.gethostbyname(hostName)
        print("IP Address: ",host_IP,"\n")
    except:
        print("Unable to get IP address from host name!","\n")

#take input for host name
hostName = input("\nEnter domain/host name: ")
get_HOST_Name_from_IP_Address(hostName)

ip_addr=input('Enter the IP address: ')

try:
    print(socket.gethostbyaddr(ip_addr))
except:
    print("Unable to get the host name from the IP address!","\n")