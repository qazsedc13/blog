Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list ('spisok')
['s', 'p', 'i', 's', 'o', 'k']
>>> a = ['1','2', 1,2]
>>> a
['1', '2', 1, 2]
>>> a[0]
'1'
>>> a[1:3]
['2', 1]
>>> a[:3]
['1', '2', 1]
>>> a[:0]=[1232354, 4534]
>>> a
[1232354, 4534, '1', '2', 1, 2]
>>> a=[1,5,3,66,33]
>>> a.sort()
>>> a
[1, 3, 5, 33, 66]
>>> a.revers()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.revers()
AttributeError: 'list' object has no attribute 'revers'
>>> a.reverse
<built-in method reverse of list object at 0x02CDD7B0>
>>> a
[1, 3, 5, 33, 66]
>>> a.reverse()
>>> a
[66, 33, 5, 3, 1]
>>> a.index(5)
2
>>> a[:]=[]
>>> a
[]
>>> a.clear()
>>> a
[]
>>> len(a)
0
>>> a.append('555')
>>> a
['555']
>>> a.remove('555')
>>> a
[]
>>> a.append('555')
>>> a
['555']
>>> del [0]
SyntaxError: can't delete literal
>>> del a[0]
>>> a
[]
>>> per = {'name':'ira', 'lastname':'kopylova']
SyntaxError: invalid syntax
>>> per = {'name':'ira', 'lastname':'kopylova'}
>>> per ['age']=25
>>> per['name']
'ira'
>>> 'name' in per
True
>>> for key, value in per.items():
	print(key,value)

	
name ira
age 25
lastname kopylova
>>> a=tuple('any string')
>>> a
('a', 'n', 'y', ' ', 's', 't', 'r', 'i', 'n', 'g')
>>> 
>>> 
>>> 
>>> #разница между списком и кортежем
>>> a=(1,2,3,)
>>> b=[1,2,3]
>>> a.__sizeof__
<built-in method __sizeof__ of tuple object at 0x02F3A0D0>
>>> a._sizeof_()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a._sizeof_()
AttributeError: 'tuple' object has no attribute '_sizeof_'
>>> a.__subclasshook__
<built-in method __subclasshook__ of type object at 0x56A993E0>
>>> 
>>> 
>>> 
>>> 
>>> a.__sizeof__()
24
>>> b.__sizeof__()
32
>>> # Кортеж занимает 24 байта, список 32
