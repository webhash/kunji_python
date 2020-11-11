'''
This is also a comment
'''

print("Hello World!!")
print()
print('-----------------------')
print()

print(note:= 'python has support for conditional construct via if-elif-else and ternary operator')

print(note:='lets create three objects')
print(one:=1)
print(two:=2)
print(three:=3)

print(note:= 'type of above object are')
print(note:= str(type(one)))
print(note:= str(type(two)))
print(note:= str(type(three))) 

print()
print('-----------------------')
print()

print(note:='lets compare the above objects via simple if/else conditional')
if two > one:
	print(note:='two is greater than one')
else:
	print(note:='two is smaller or equal to one')


print()
print('-----------------------')
print()

print(note:='we can also nest the if-else conditional')

if two> one:
	print(note:='two is greater than one')
	if three > two:
		print(note:='three is greater than two')
	else:
		print(note:='three is smaller or equal to two')
else:
	print(note:='two is smaller or equal to one')
	

print()
print('-----------------------')
print()


print(note:='we can change the above nested if else to elif conditional')
if two <= one:
	print(note:='two is smaller or equal to one')
elif three <= two:
	print(note:='three is smaller or equal to two')
else:
	print(note:='two is greater than one')
	print(note:='three is greater than two')

print()
print('-----------------------')
print()


print(note:='python also supports X if (condition) else Y')
print(note:='two is greater than one') if (two > one) else print(note:='two is smaller or equal to one')

print()
print('-----------------------')
print()

print(note:='python also uses interning for numbers')
print(note:='All of this for optimization')
print(hex(id(one)), end= ' == ')
print(hex(id(1)))

print(hex(id(two)), end= ' == ')
print(hex(id(2)))

print(hex(id(three)), end= ' == ')
print(hex(id(3)))


assert hex(id(one)) == hex(id(1))
assert hex(id(two)) == hex(id(2))
assert hex(id(three)) == hex(id(3))


print()
print('-----------------------')
print()
