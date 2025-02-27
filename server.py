import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 7070)

print(f"starting up {server_address}")
sock.bind(server_address)

sock.listen(1)

def encode_msg(message):
    msg_converted = ""
    for i in message:
        msg_converted += chr((ord(i) + 1) % 256)
    return msg_converted

while True:
    print("waiting")
    connection, client_address = sock.accept()

    try:
        print(f"connection from {client_address}")
        while True:
            # no more than 256 characters for a message
            data = connection.recv(256)
            print(f"received {data}")
            if data:
                print("message received")
                # msg = str(data)
                msg = data.decode('utf-8')
                print(f"encoded message: {msg}")
                # this is where we would need to convert message to the encoded message
                encoded_message = encode_msg(msg)
                print(f"encoded message: {encoded_message}")
                # converts message to bytes and sends back
                connection.sendall(encoded_message.encode('utf-8'))
            else:
                print(f"no more data from {client_address}")
                break

    finally:
        connection.close()
