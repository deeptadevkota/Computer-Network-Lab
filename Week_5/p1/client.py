import socket
import ssl

client = socket.socket()

context = ssl.SSLContext()
context.verify_mode = ssl.CERT_REQUIRED

context.load_verify_locations("certificate/ca_cert.pem")

context.load_cert_chain(certfile="certificate/client_cert.pem", keyfile="certificate/client_key.pem")

secure_socket = context.wrap_socket(client)
secure_socket.connect(("localhost",9999))

server_certficate = secure_socket.getpeercert()

if not server_certficate:
    raise Exception("\nUnable to get certificate from server")
else:
    print("\nConnected to server")
    print("Receiving..")
    print(secure_socket.recv(1024).decode())

secure_socket.close()
client.close()

print("Connection closed!\n")