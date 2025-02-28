# import socket

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server_address = ('localhost', 7070)
# print('connecting to %s port %s' % server_address)
# sock.connect(server_address)

# try:
#     #message that is being sent to server
#     message = 'Hello World'
#     print(f'sending {message}')
#     sock.sendall(bytes(message, 'utf-8'))

#     # look for a response back
#     amount_received = 0
#     amount_expected = len(message)

#     while amount_received < amount_expected:
#         #no more than 256 characters
#         data = sock.recv(256)
#         amount_received += len(data)
#         print(f'received {data}')

# finally:
#     print('closing client')
#     sock.close()


print("In client file")
import socket
import sys

# check if the user provided a message argument
if len(sys.argv) < 2:
    print("Error: Please enter a message.")
    sys.exit(1)

# get the message from the command-line argument
message = sys.argv[1]

# check if the message length is within the 256-character limit
if len(message) > 256:
    print("Error: Message exceeds 256 characters. Please enter a shorter message.")
    sys.exit(1)

# create a socket / endpoint for communication with the server
client_socket = socket.socket()

# connect to the server's address and port
server_address = ('localhost', 7070)
print('connecting to %s port %s' % server_address)

try:
    client_socket.connect(server_address)
except ConnectionRefusedError:
    # throw an error if client tries to connect without server running
    print("Error: Unable to connect to the server. Make sure the server is running.")
    sys.exit(1)


try:
    # send the message to the server
    print("sending ", message)
    client_socket.sendall(bytes(message, 'utf-8'))   # .sendall ensures entire message is sent in one go 

    # look for a response back
    data = client_socket.recv(256)
    print("received ", data)
    # convert received response from bytes to string in order to disply 
    converted = data.decode('utf-8')
    print("converted message:", converted)

finally:
    print('closing client')
    # close the communication socket on the client side
    client_socket.close()

