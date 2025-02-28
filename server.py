# import socket

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_address = ('localhost', 7070)

# print(f"starting up {server_address}")
# sock.bind(server_address)

# sock.listen(1)

# def encode_msg(message):
#     msg_converted = ""
#     for i in message:
#         msg_converted += chr((ord(i) + 1) % 256)
#     return msg_converted

# while True:
#     print("waiting")
#     connection, client_address = sock.accept()

#     try:
#         print(f"connection from {client_address}")
#         while True:
#             # no more than 256 characters for a message
#             data = connection.recv(256)
#             print(f"received {data}")
#             if data:
#                 print("message received")
#                 # msg = str(data)
#                 msg = data.decode('utf-8')
#                 print(f"encoded message: {msg}")
#                 # this is where we would need to convert message to the encoded message
#                 encoded_message = encode_msg(msg)
#                 print(f"encoded message: {encoded_message}")
#                 # converts message to bytes and sends back
#                 connection.sendall(encoded_message.encode('utf-8'))
#             else:
#                 print(f"no more data from {client_address}")
#                 break

#     finally:
#         connection.close()


print("In server file")
import socket

# server creates a socket / ommunication endpoint that waits for connections -- specifies ipv4 addressing and tcp
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server uses bind to assign the socket to specific ip address and port number
server_socket_addr = ('localhost', 7070)
server_socket.bind(server_socket_addr)

# server tells the system it is ready to accept connections
server_socket.listen(1)

# define function for encoding message -- each letter in message converted to next ascii character
def encode_msg(message):
    msg_converted = ""
    for i in message:
        msg_converted += chr(ord(i) + 1)
    return msg_converted

def start_server():
    try:
        # keep the server running continously to accept multiple client connections
        while True:
            # server waits until a client tries to connect
            print("waiting")
            # when a client connects, server calls accept which creates a new socket/address for actual communication
            connection, client_address = server_socket.accept()
            print("connection from ", client_address)

            try:
                # receive message from the client (already restricted to less than 256 characters from client side)
                data = connection.recv(256)
                print("received ", data)

                # if data exists, server processes it
                if data:
                    # convert message from bytes into string
                    msg = data.decode('utf-8')
                    print("encoding message...")
                    # encode the message ascii characters
                    encoded_message = encode_msg(msg)
                    print("sending ", encoded_message)
                    # converts message into bytes again and sends back
                    connection.sendall(encoded_message.encode('utf-8'))
                else:
                    print("No more data from ", client_address)
                    break

            finally:
                # close the communication socket on the server side
                connection.close()

    except KeyboardInterrupt:
        # finally close the listening socket on the server side
        print("\nClosing server listening socket...")
        server_socket.close()

if __name__ == '__main__':
    start_server()


