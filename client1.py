import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 7070)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    #message that is being sent to server
    message = 'Hello World'
    print(f'sending {message}')
    sock.sendall(bytes(message, 'utf-8'))

    # look for a response back
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        #no more than 256 characters
        data = sock.recv(256)
        amount_received += len(data)
        print(f'received {data}')

finally:
    print('closing client')
    sock.close()