Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1='hello'
s1
'hello'
type(s1)
<class 'str'>
s1.capitalize()
'Hello'
s1.upper()
'HELLO'
s1.lower()
'hello'
s1='hEllo'
s1.casefold()
'hello'
s1='HeLLo'
s1.casefold()
'hello'
s1.count()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s1.count()
TypeError: count expected at least 1 argument, got 0
s1.count('i')
0
s1.count('L')
2
s1.count('H')
1
s1.endswith('o')
True
s1.find('L')
2
s1.find('o')
4

s1.index('o')
4
s1.index('m')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s1.index('m')
ValueError: substring not found
s1.isalpha()
True
s1.isdigit()
False
s1.join('there')
'tHeLLohHeLLoeHeLLorHeLLoe'
s1.removeprefix('L',"I")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s1.removeprefix('L',"I")
TypeError: str.removeprefix() takes exactly one argument (2 given)
s1='how are you'
s1
'how are you'
s1.split('')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    s1.split('')
ValueError: empty separator
s1.split('')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s1.split('')
ValueError: empty separator
s1.split('-')
['how are you']
s1.swapcase()
'HOW ARE YOU'
s1='hello there!!!'
len(s1)
14
s1[3]
'l'
s1[-16]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s1[-16]
IndexError: string index out of range
s1[0:5]
'hello'
s1[2:12:2]
'lotee'
s1[-15:-10]
'hell'
s1[-10::-2]
'olh'
s1[::-2]
'!!rh le'

s1
'hello there!!!'
>>> 
============== RESTART: C:/wipro traning/python/str1.py =============
h
e
l
l
o
 
t
h
e
r
e
>>> 
============== RESTART: C:/wipro traning/python/str1.py =============
h
e
l
l
o
>>> 
============== RESTART: C:/wipro traning/python/str1.py =============
h
e
l
l
o
 
t
h
e
r
e
