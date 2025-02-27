import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 7070)

print(f"starting up {server_address}" )
sock.bind(server_address)

sock.listen(1)

while True:
    print("waiting")
    connection, client_address = sock.accept()

    try:
        print(f"connection from {client_address}")
        while True:
            #no more than 256 characters for a message
            data = connection.recv(256)
            print(f"received {data}")
            if data:
                print("message received")
                msg = str(data)
                #this is where we would need to convert message to the encoded message
                

                msg = bytes(msg, 'utf-8')
                connection.sendall(msg)
            else:
                print(f"no more data from {client_address}")
                break

    finally:
        connection.close()