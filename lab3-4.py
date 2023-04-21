from bs4 import BeautifulSoup
import requests

URL = "http://biik.ru/rasp/cg109.htm"
a = requests.get(URL)
a.encoding="windows-1251"#для кодировки русского языка
if a == 404:
	print ('Not Found')
else: 
	all_web_code = a.text#весь полученный текст с тегами
	bs =BeautifulSoup(all_web_code,"html.parser")
	Lesson = bs.findAll('td')#находим все тэги td так как там расписание
	
	file = open ("Raspisanie.txt", "w")#создаем и записываем
	for item in Lesson:
		file.write(item.text +"\n")
	file.close()

	line = open ("Raspisanie.txt").readlines()#лайн будет нужен для корректной записи в файл(так как будут пробелы)
	for i in line:
		line.pop(0)
	
	f = open ("Raspisanie.txt", "w")
	for i in line:
		f.write(i)#записываем
	f.close()
fout = open ("Raspisanie.txt", "r")#чтобы прочитать файл в консоли
print(fout.read())


