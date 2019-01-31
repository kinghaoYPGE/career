import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 8089))
s.listen(1)
sock, addr = s.accept()
print('connecting...')
msg = sock.recv(1024).decode()
name = input('your name: ')
while msg != 'exit':
    print('%s: %s' % (name, msg))
    send_msg = input()
    sock.send(send_msg.encode('utf-8'))
    if send_msg == 'exit':
        break
    msg = sock.recv(1024).decode()
sock.close()
s.close()