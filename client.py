import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Write IP address of Server: ')
ips = input () #ввод ip адресса
print ('Write Port of Server: ')
port = (int(input())) #вводим порт
sock.connect((ips, port)) #коннект
while True:
    print ('Write the massage you want to send: ') 
    ms = input() #ввод сообщения
    sock.send(bytes(ms, encoding = 'UTF-8')) #перевод сообщения в байт
    data = sock.recv(1024) #ожидание ответа
    print(f'Server give answer: ',str(data)[2:-1]) #вывод сообщения сервера