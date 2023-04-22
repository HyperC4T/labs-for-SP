import socket

HOST = '192.168.0.17'  # ip адресс
PORT = 9090       # порт (non-privileged ports are > 1023)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) #связываем адресс и порт
    s.listen() #переводит сервер для приема подключений
    conn, addr = s.accept() #принимаем соединение
    with conn:
        print('Connected by', addr) #выводим адрес к которому подключились
        while True:
            data = conn.recv(1024) #получаем данные из сокета(макс обьем данных)
            if not data:#если ничего нет,то все завершается
                break
            print(f'{addr[0]} send: ',str(data)[2:-1]) #вывод сообщения
            conn.sendall(bytes('i read your message', encoding = 'UTF-8')) #отправляем в клиент