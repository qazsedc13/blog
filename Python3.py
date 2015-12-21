Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> per=123
>>> if per<100:
	print('per<100')
	elif per>200:
		
SyntaxError: invalid syntax
>>> per
123
>>> if per < 100:
	print('per < 100')
elif per > 200:
	print('per > 200')
else:
	print('per=123')

	
per=123
>>> if True and False:
	1

	
>>> if True or False:
	1

	
1
>>> if not True:
	1

	
>>> 
>>> 
>>> 
>>> a=1
>>> while a!=3
SyntaxError: invalid syntax
>>> while a!=3:
	print(a)
	a+=1

	
1
2
>>> a=1
>>> while a!=3:
	print (a, end=' ')
	a+=1

	
1 2 
>>> 
>>> 
>>> 
>>> a=['1', '2', '3']
>>> for x in a:
	print(x)

	
1
2
3
>>> for i in range (5):
	print (i)

	
0
1
2
3
4
>>> for i in range (3,7):
	print(i)

	
3
4
5
6
>>> for i in 'string o string':
	if i == 'o':
		continue
	print(i*2, end='')

	
ssttrriinngg    ssttrriinngg
>>> for i in 'string o string':
	if i == 'o':
		break
	print(i*2, end='')

	
ssttrriinngg  
>>> 
