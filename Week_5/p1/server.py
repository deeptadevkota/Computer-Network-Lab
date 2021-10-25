import socket
import ssl


server = socket.socket()

server.bind(("localhost",9999))
server.listen(5)

print("Server is listening....")

contex = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

while True:
    client, address = server.accept()

    secure_socket = ssl.wrap_socket(client, 
                                    server_side=True, 
                                    ssl_version=ssl.PROTOCOL_TLS, 
                                    ca_certs="certificate/ca_cert.pem",
                                    certfile="certificate/server_cert.pem",
                                    keyfile="certificate/server_key.pem",
                                    cert_reqs=ssl.CERT_REQUIRED)
    
    client_certificate = secure_socket.getpeercert()

    if not client_certificate:
        raise Exception("\nUnable to get certificate from client")
    else:
        print("\nCertificate of client ", address, " received")
        print("Client name: ",secure_socket.recv(1024).decode())
        secure_socket.send(bytes('You now have a secured connection!','utf-8'))
    
    secure_socket.close()
