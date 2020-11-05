print("Hello World!!")


print()
print('-----------------------')
print()

print(note:= 'python has many built in functions like len, str, type, etc')
print('Length of note is ' + str(len(note)))
print('Type of note is ' + str(type(note)))

print()
print('-----------------------')
print()

print(note:='we can create our own function also')
print(note:='def is used to tell interpretor/complier that we are creating a new function')

# __name__ can be used to get the name of the function as string
def something():
	print(note:='we are inside the ' + something.__name__ + ' function')
	return 'yay'


print()
print('-----------------------')
print()


print(note:='we can call the above function by using the something()')
something()
print(note:='we capture the return value of the function')
print(note:=something())


print()
print('-----------------------')
print()


print(note:='In python function are first class object, that is to say they can be passed around as variable or assigned to other variables')
print('Type of something is ' , type(something))

new_something = something 
print('Type of new_something is ' , type(new_something))
print('Both function points to the same memory address')
print(hex(id(new_something)))
print(hex(id(something)))
assert hex(id(new_something)) == hex(id(something))

print(note:='if we call new_something it would call the something function')
new_something()

print()
print('-----------------------')
print()

print(note:='we can pass parameters to the functions')
def new_something(some):
	print(note:='we are inside the ' + new_something.__name__ + ' function')
	print(some)
	# this function shall return the None 

print(note:='python doesnt force the type requirement on parameter')
new_something(1)
new_something('wow')

print(note:='python function always return a value, if you dont specify anythin it will return None')
print(note:=new_something('yay'))

print()
print('-----------------------')
print()



print(note:='python also supports the lamdas - basically nameless function ')

some_func = lambda some: print(some)

some_func('yay')

print(note:=some_func('wow'))

print()
print('-----------------------')
print()


print(note:='lets quicly touch the peephole optimization done in python')

def peep_func():
	x = 500*10
	y = 'welcome'*4
	if 1 in [ 1,2,3,4,5,6 ]:
		print('yes')
	else:
		print('no')

print(peep_func.__code__.co_consts)
print(note:= ' as you can see above python creates the constants for variables and membership tests so that optimization can happen')
print(note:= ' python also converts the list to tuples for membership') 

print()
print('-----------------------')
print()


print(note:='lets look at the mutability of arguments passed to function')

def mod_function(var):
	if (type(var)) is str:
		print(note:='Inside the mod_function')
		print(var)
		print(hex(id(var)))
		var = var.upper()
		print(var)
		print(hex(id(var)))
	else: 
		print('please pass a string')

some_string = 'wElCoMe'
print(note:='string before function call')
print(some_string)
print(hex(id(some_string)))
mod_function(some_string)
print(note:='string after function call')
print(some_string)
print(hex(id(some_string)))
print('As you can see above that mod_function had the reference to the some_string, it modified it, but new copy was created')

print()
print('-----------------------')
print()

def mod_function_2(var):
	if (type(var)) is list:
		print(note:='Inside the mod_function')
		print(var)
		print(hex(id(var)))
		var.append('welcome')
		print(var)
		print(hex(id(var)))
	else: 
		print('please pass a list')

some_list = ['yes', 'no', '1']
print(note:='list before function call')
print(some_list)
print(hex(id(some_list)))
mod_function_2(some_list)
print(note:='list after function call')
print(some_list)
print(hex(id(some_list)))
print('As you can see above that mod_function had the reference to the some_list, it modified it, and we see the change outside the function because list is of mutable type')

print()
print('-----------------------')
print()
