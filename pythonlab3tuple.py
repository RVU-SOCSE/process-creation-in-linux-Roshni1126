Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=(10,20,30,50)
>>> a
(10, 20, 30, 50)
>>> a=(10,20,'anu',20.4)
>>> a[10,20,30,20,20,40]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a[10,20,30,20,20,40]
TypeError: tuple indices must be integers or slices, not tuple
>>> a.append(30)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a.append(30)
AttributeError: 'tuple' object has no attribute 'append'
>>> a[10,20,30,20,20,40]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a[10,20,30,20,20,40]
TypeError: tuple indices must be integers or slices, not tuple
>>> 
>>> 
>>> a=(10,20,30,20,20,40)
>>> a
(10, 20, 30, 20, 20, 40)
>>> a.count(20)
3
>>> a.index(30)
2
>>> len(a)
6
>>> max(a)
40
>>> min(a)
10
