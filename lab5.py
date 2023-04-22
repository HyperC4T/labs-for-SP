from ftplib import FTP

ftp = FTP('ftp.gnu.org')

ftp.login()


# Путь на нашем компьютере где сохранить файл.
out = 'C:\\Users\\HYPERC4T\\Desktop\\tree.json.gz'

with open(out, 'wb') as f:
    ftp.retrbinary('RETR ' + 'tree.json.gz', f.write)
