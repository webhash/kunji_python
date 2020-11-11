
print("Hello World!!")


print()
print('-----------------------')
print()

print(note:='The yield statement suspends function’s execution and sends a value back to the caller')
print(note:='but it retains enough information to enable function to resume where it is left off.')
print(note:='When resumed, the function continues execution immediately after the last yield run.')

print(note:='let us create a function that yields values')

def some_gen():
	yield 'yes'
	yield 'no'
	yield 'maybe'
	yield 'never'

print(note:='any function that has yield in it considered/becomes a generator')
something = some_gen()
print(next(something))
print(next(something))
print(next(something))
print(next(something))

try:
	print(next(something))
except StopIteration:
	print(note:='as we have no more values to yield we shall get the StopIteration error')

print()
print('-----------------------')
print()


print(note:='we can also use the for loop')

for value in some_gen():
	print(value)
	
def pow2_gen():
	i = 1
	while True:
		yield 2**i
		i+=1
	

for value in pow2_gen():
	if(value < 100):
		print(value)
	else:
		break;

print()
print('-----------------------')
print()


print(note:='Lets create Fibonacci series with generators')

print(note:='this function will perform faster than a normal recursive or iterative implementation of series')

def fibonacci(n):
	f0 = 0
	yield f0
	f1 = 1
	yield 1
	for i in range(n-2):
		f0, f1 = f1, f0 + f1
		yield f1

print([n for n in fibonacci(50)])


print()
print('-----------------------')
print()