import socket

while True:
    port = input('������� ���� �� 1024 �� 65535: \n')
    if not port.isnumeric():
        print('������')
    elif 1023 <= int(port) <= 65535:
        break
    else:
        print('������: ���� �� ������ � ������ ��������')

while True:
    address = input('������� ip ������� ��� �������� ������ ��� �������� localhost: \n')
    if address == '':
        address = 'localhost'
        break
    else:
        break

sock = socket.socket()
sock.setblocking(True)
sock.connect((address, int(port)))

auth = sock.recv(1024).decode()
print(auth)
if auth[0] == 'I':
    sock.send(input().encode())
    print(sock.recv(1024).decode())
    sock.send(input().encode())
else:
    print(sock.recv(1024).decode())
while True:
    sock.send(input().encode())
    answer = sock.recv(1024).decode()
    print(answer)
    if answer[0] == 'C':
        break

while True:
    mesg = input("Input message: ")
    if mesg == "exit":
        sock.close()
        break
    sock.send(mesg.encode())
    data = sock.recv(1024)