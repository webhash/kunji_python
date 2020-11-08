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

print(note:='lets have look at docstring and annotation')
print(note:='python has a help function to shows us details and providea glimpse into the functionality of thing under consideration')
print(note:='help for print shows below output')
help(print)
print()
print(note:='pretty cool ...eh ?')

def to_upper(input):
	if type(input) == str:
		print(input.upper())
	else:
		print('please pass a string as input')

print(note:='what would happen if we run help on above function?')
print()
help(to_upper)
print()
print(note:='As you can see we dont have much help information')
print()
print(note:='we can add docstring to our own functions so that when help is called on it, we print the requested information')

def to_upper_with_help(input):
	# this is a docstring that shall be consumed by help function
	'''
	prints the upper case of the string passed
	if no string passed we shall update the user that we expect a string input'
	Inputs:
		string
	Returns:
		upper case of string
	'''
	if type(input) == str:
		print(input.upper())
	else:
		print('please pass a string as input')
		
print(note:='Now when we shall do help on the above function we shall see the information')
print()
help(to_upper_with_help)
print()
print(note:='How does the help picks this information???')
print(note:='lets do dif on the function and see if we can get some hint')
print()
print(dir(to_upper_with_help))
print()
print(note:='did you notice the __doc__ attribute in above result?, if we print it we shall see the same content that help throws')
print(to_upper_with_help.__doc__)
print()
print(note:='did you notice the __annotations__ attribute in dir result? currently its empty')
print(to_upper_with_help.__annotations__)
print()
print(note:='lets create another function that supports annotation')
def to_upper_with_annotation(input:'annotation for input, we expect a string as input')->'annotation for return value, we dont return anything from this function':
	# this is a docstring that shall be consumed by help function
	'''
	prints the upper case of the string passed
	if no string passed we shall update the user that we expect a string input'
	Inputs:
		string
	Returns:
		upper case of string
	'''
	if type(input) == str:
		print(input.upper())
	else:
		print('please pass a string as input')
		
print()
print(note:='and now we will see the information in annotation attribute')
print(to_upper_with_annotation.__annotations__)
print(note:='now if we do help on the above function we shall see both the docstring and annotation')
print()
help(to_upper_with_annotation)
print()
print('-----------------------')
print()


print(note:='python supports many inbuilt function which can come handy')
print(note:='like min, max, sum, any ')

print(note:='sum - returns the sum of all the values')
print(sum([ i for i in range(0,6)]))
print(note:='max - returns the max value')
print(max([ i for i in range(0,6)]))
print(note:='min - returns the min value ')
print(min([ i for i in range(0,6)]))
print(note:='any - returns true if at least one value is non None type ')
print(any([ i for i in range(0,6)]))

print()
print('-----------------------')
print()

print(note:='lets have another look at the lambdas we touched earlier')

f =  lambda x,y : x**y 
print(note:='lambda is a nameless function, the variable points to the lambda function created')
print(note:='we can call this function by using the variable passing required parameters')
print(f(2,3))
assert f(2,2) == 4
print(note:='lambdas allows default parameters')

f = lambda x, y=2 : x**y 
print(f(2))
assert f(2) == 4 

print(note:='as we mentioned before function are first class object, we can pass them as variable')
print(note:='check the below function, here we pass two variable, first one is used as an argument to the lambda function passed to it as second parameter')

def use_lambda(x,lm):
	print(lm(x))

use_lambda(2,f)


print(note:='higher order function is a function that takes function as argument and can return function as a result')
print(note:='map and filter  are example of such functions')

print()
print('-----------------------')
print()
print(note:='map can be used to apply a function to iterables')
print(note:='map returns iterables, with function applied to each input in the iterable passed to it')
print(list(map(f, [2,4,8])))
print(note:='our lambda function can take two arguments, and map also can take multiple iterables')
print(list(map(f, [2,3,4], [2,3,4])))
print(note:='if number of elements are not same in the two iterables passed, we shall get limited results')
l = list(map(f, [1,2,3,4,5,6], [2,3]))
print(l)
l = list(map(f, [0,1,2,3,4,5], [1,2,3,1,2,3]))
print()
print('-----------------------')
print()

odd = lambda x : x%2
print(note:='filter is used to filter iterables based on truthfulness or function passed to it')
print(list(filter(odd, l)))
print(list(filter(None, l)))



print()
print('-----------------------')
print()