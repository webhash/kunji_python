print("Hello World!!")


print()
print('-----------------------')
print()



print(note:='Parameters are defined by the names that appear in a function definition')
def func(foo, bar):
	print(foo)
	print(bar)
print(note:='foo and bar are the parameters')
print(note:='whereas arguments are the values actually passed to a function when calling it.')
func(42, 'life')
print(note:='42 and `life` are the arguments')
print(note:='if function expects argument and you don`t pass them then it will cause the TypeError')
print(note:='As function "type" expected the arguments') 

print()
print('-----------------------')
print()

print(note:='but don`t worry python supports the default arguments')
print(note:='so if we don`t pass the arguments for default value parameters python shall use the default value')
def func2(foo, bar='life', woo='work', har='hard'):
	print(foo)
	print(bar)
	print(woo)
	print(har)

print(note:='here we are passing `love` as first argument, python know that the first parameter is foo, and thus assigns the value to it')
func2('love')
print(note:='and for the other params it uses the default values')

print(note:='but once a parameter is assigned a default value, all parameters after it  must be asigned a default values too')
print(note:='func3(foo, bar="life", woo, har) will throw SyntaxError')

print(note:='we can also use the name of the parameter to assign the argument values ')
print(note:='and thus dont rely on the position of parameters')

func2(har='HaRd', bar='LOVE', woo='WORK', foo='life')

print(note:='but once named argument is used all arguments after it must also be named')

print(note:='func2(foo="life", bar="LOVE", woo="WORK", "SMART")')

print(note:='we will get Syntax error for above as we have to use the named arguments for "har" parameter')

print(note:='but we can omit the "har" parameter as it has a default value and python shall pick that if no argument passed')
func2(bar='LOVE', woo='WORK', foo='life')


print()
print('-----------------------')
print()

