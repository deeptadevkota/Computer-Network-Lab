import socket


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_IP='localhost'
PORT=8000
server.bind((HOST_IP,PORT))
server.listen(3)

print('HTTP server is listening..')


def handle_request(request):
    """Handles the HTTP request."""

    headers = request.split('\n')
    filename1 = headers[0].split()[1]


    filename=filename1[1:len(filename1)]


    try:
        fin = open(filename)
        content = fin.read()
        fin.close()

        response = 'HTTP/1.0 200 OK\n\n' + content
    except FileNotFoundError:
        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'

    return response

while True:
    client,addr=server.accept()
    request=client.recv(1024).decode()
    response=handle_request(request)
    client.sendall(response.encode())
    client.close()

server.close()