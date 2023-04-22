import ftplib
import os
import time
from tkinter import filedialog
import tkinter
import tabulate

def init():
    # очистка экрана и объявление глобальных переменных
    os.system('CLS')
    global ftp
    global root

    # tkinter нужен для диалоговых окон
    root=tkinter.Tk()
    root.withdraw()

    # ввод Ip адреса ftp сервера, имени пользователя и пароля
    SERVER = str(input("IP: "))
    USER = str(input("User: "))
    PASS = str(input("Password: "))

    # попытка подключения к серверу
    try:
        ftp = ftplib.FTP(SERVER)
        ftp.login(USER, PASS)
        print()
        print(f"[OK] Соединение с {SERVER} установлено!")
        print()
        time.sleep(5)
        # в случае удачного соединения вызывается основная функция
        maindef()
    except:
        print()
        print(f"[ERROR] Ошибка соединения с {SERVER}!")
        print(f"[ERROR] Проверьте правильность введеных данных!")
        print()
        time.sleep(5)
        # в случае ошибки функция init() повторится
        init()

def fil_size():
    filenames = []
    ftp.retrlines('LIST', lambda line: filenames.append(line.split()))
    data = [
        ['Имя', 'Размер', 'Дата изменения'],
    ]

    for file in filenames:#для таблицы с файлами
        te=float(file[2])
        cont=0
        while te>=1024:
            te/=1024
            cont+=1
        if cont==0:
            dat="Байт"
        if cont==1:
            dat="Кб"
        if cont==2:
            dat="Мб"
        if cont==3:
            dat="Гб"
        dat2=[
            file[3], str(float('{:.3f}'.format(te)))+dat, file[1]+" "+file[0]
        ]
        data.append(dat2)
    print()
    results = tabulate.tabulate(data)
    return results

def maindef():
    print()
    print(fil_size())
    print()
    file = str(input('Какой файл скачаем с сервера: '))
    dir = filedialog.askdirectory()
    with open(dir+"\\"+file, 'wb') as f:
            ftp.retrbinary('RETR ' + file, f.write)
            print()
            print(f"[OK] Файл: {file} был скачан в {dir}/{file}")
            print()
            time.sleep(5)  
    ftp.close

# начало выполнения
if __name__ == "__main__":
    init()
