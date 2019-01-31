import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8089))
print('connecting...')
name = input('your name: ')
msg = ''
while msg != 'exit':
    print('%s:%s' % (name, msg))
    send_msg = input()
    s.send(send_msg.encode('utf-8'))
    if send_msg == 'exit':
        break
    msg = s.recv(1024).decode()
s.close()