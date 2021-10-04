import socket

# function get host id from host name
def get_HOST_Name_from_IP_Address(hostName):
    try:
        host_IP = socket.gethostbyname(hostName)
        print("IP Address: ",host_IP)
    except:
        print("Unable to get IP address from host name!")

#take input for host name
hostName = input("Enter domain/host name: ")
get_HOST_Name_from_IP_Address(hostName)