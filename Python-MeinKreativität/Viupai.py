Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\Giova\AppData\Local\Programs\Python\Python38\GioPython\Startseite.py
>>> f = open('GioPython/Startseite.py', 'w')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    f = open('GioPython/Startseite.py', 'w')
FileNotFoundError: [Errno 2] No such file or directory: 'GioPython/Startseite.py'
>>>  f = open('/GioPython/Startseite.py', 'w')
 
SyntaxError: unexpected indent
>>> f = open('/GioPython/Startseite.py', 'w')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    f = open('/GioPython/Startseite.py', 'w')
FileNotFoundError: [Errno 2] No such file or directory: '/GioPython/Startseite.py'
>>> f=open('C:/Users/Giova/AppData/Local/Programs/Python/Python38/GioPython/Startseite.py', 'w')
>>> print(f)
<_io.TextIOWrapper name='C:/Users/Giova/AppData/Local/Programs/Python/Python38/GioPython/Startseite.py' mode='w' encoding='cp1252'>
>>> Finalmente = 'Uma resposta sem erro!'
>>> if alavanca == True :
	print('Viu pai')

	
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    if alavanca == True :
NameError: name 'alavanca' is not defined
>>> if Finalmente == 'Uma resposta sem erro!' :
	print('Viu pai')

	
Viu pai
>>> 
