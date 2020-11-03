
print("Hello World!!")

print()
print('-----------------------')
print()

print(note:='lets create a string')
print(some_string:='this is a string')


try:
	# index starts from 0 thus len -1
	if some_string[len(some_string) - 1] == 'g':
		print(note:='this shall be executed')
except IndexError:
	print(note:='if we have the Index error this shall be executed')
else:
	print('No exception was raised this time, we will execute the else block')
finally:
	print(note:='finally is always be executed')
	
print()
print('-----------------------')
print()

try:
	# this will case the index error as we overshoot the length of string
	if some_string[len(some_string)] == 'g':
		print(note:='this shall not be executed')
except IndexError:
	print(note:='We will get the Index error')
else:
	print('exception was raised this time, we shall not execute the else block')
finally:
	print(note:='finally is always be executed')

print()
print('-----------------------')
print()