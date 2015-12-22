Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def func(x):
	if x>0:
		print('x>0')
	else:
		print('x<=0')

		
>>> func(3)
x>0
>>> func(0)
x<=0
>>> func(-5)
x<=0
>>> def func(x):
	return x*2

>>> a = func(5)
>>> a
10
>>> def func():
	pass

>>> print(func())
None
>>> 
>>> 
>>> 
>>> def(a, b, c=2):
	
SyntaxError: invalid syntax
>>> def func(a, b, c=2):
	return a+b+c

>>> func(2, 5)
9
>>> func(1, 2, 3)
6
>>> def func(*args):
	return args

>>> func(1,5, 45, 'ASDF')
(1, 5, 45, 'ASDF')
>>> 
