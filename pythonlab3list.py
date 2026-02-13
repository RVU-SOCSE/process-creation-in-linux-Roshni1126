Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[10,20,30,40]
>>> b=[10,"anu",10.2,True]
>>> a
[10, 20, 30, 40]
>>> b
[10, 'anu', 10.2, True]
>>> a.append(100)
>>> a
[10, 20, 30, 40, 100]
>>> c=a.copy()
>>> c
[10, 20, 30, 40, 100]
>>> a.append(10)
>>> a
[10, 20, 30, 40, 100, 10]
>>> a.count(10)
2
>>> a.extend([200,300,400])
>>> a
[10, 20, 30, 40, 100, 10, 200, 300, 400]
>>> a.index(100)
4
>>> a.insert(5,150)
>>> a
[10, 20, 30, 40, 100, 150, 10, 200, 300, 400]
>>> a.pop()
400
>>> a.pop(1)
20
>>> a
[10, 30, 40, 100, 150, 10, 200, 300]
>>> a.remove(40)
>>> a
[10, 30, 100, 150, 10, 200, 300]
>>> a.sort()
>>> a
[10, 10, 30, 100, 150, 200, 300]
>>> a.reverse()
>>> s
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> a
[300, 200, 150, 100, 30, 10, 10]
>>> a.clear()
>>> a
[]
