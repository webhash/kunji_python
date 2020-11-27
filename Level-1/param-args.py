print("Hello World!!")

print()
print('-----------------------')
print()

print(note := 'Parameters are defined by the names that appear in a function definition')


def func(foo, bar):
    print(foo)
    print(bar)


print(note := 'foo and bar are the parameters')
print(note := 'whereas arguments are the values actually passed to a function when calling it.')
func(42, 'life')
print(note := '42 and `life` are the arguments')
print(note := 'if function expects argument and you don`t pass them then it will cause the TypeError')
print(note := 'As function "type" expected the arguments')

print()
print('-----------------------')
print()

print(note := 'but do not worry python supports the default arguments')
print(note := 'so if we do not pass the arguments for default value parameters python shall use the default value')


def func2(foo, bar='life', woo='work', har='hard'):
    print(foo)
    print(bar)
    print(woo)
    print(har)


print(note := 'here we are passing `love` as first argument, \
python know that the first parameter is foo, and thus assigns the value to it')
func2('love')
print(note := 'and for the other params it uses the default values')

print(note := 'but once a parameter is assigned a default value, \
all parameters after it  must be assigned a default values too')
print(note := 'func3(foo, bar="life", woo, har) will throw SyntaxError')

print(note := 'we can also use the name of the parameter to assign the argument values ')
print(note := 'and thus do not rely on the position of parameters')

func2(har='HaRd', bar='LOVE', woo='WORK', foo='life')

print(note := 'but once named argument is used all arguments after it must also be named')

print(note := 'func2(foo="life", bar="LOVE", woo="WORK", "SMART")')

print(note := 'we will get Syntax error for above as we have to use the named arguments for "har" parameter')

print(note := 'but we can omit the "har" parameter as it has a default value and \
python shall pick that if no argument passed')
func2(bar='LOVE', woo='WORK', foo='life')

print()
print('-----------------------')
print()

print(note := 'many a times function consumes multiple arguments, and it could become messy to deal with each of them')
print(note := 'but do not worry python has solution for that ... say hello to  *')
print(note := 'although iteratable unpacking returns a list, \in context of function it returns tuple, \
which makes sense as python would not want you to change the arguments passed by user')


def sums_1(foo, bar, *args):
    print(foo)
    print(bar)
    print(type(args))
    print(args)
    s = foo + bar + sum(args)
    print('total sum is ', s)


sums_1(1, 2, 3, 4, 5)
print(
    note := 'one can use any valid param name instead of args, but sticking to standard nomenclature \
    makes your code more readable')


def sums_2(*anything):
    if len(anything):
        print(type(anything))
        print(anything)
        print('total sum is ', sum(anything))


sums_2(1, 2, 3, 4, 5)

print(note := 'lets quickly have a look at the below function')


def sum_3(*args, flag=False):
    if len(args):
        print(type(args))
        print(args)
        print('total sum is ', sum(args))
    if flag:
        print('we raise the flag')


print(note := 'this function works for all the following scenarios')
print()
print(note := 'if nothing is passed we use the default flag value, if we had not assigned the False\
as default value we will get TypeError')
sum_3()
print(note := 'we can pass just the flag value')
sum_3(flag=True)
print(note := 'we can pass arguments and skip the flag variable')
sum_3(1, 2, 3, 4, 5)
print(note := 'and lastly we can pass both the args and flag')
sum_3(1, 2, 3, 4, 5, flag=True)

print()
print('-----------------------')
print()

print(note := 'remember the double asterisks ? yes **')
print(note := '** can be used to consume both the param name and the argument value passed by the user.')


def sum_4(**kwargs):
    if len(kwargs):
        print(type(kwargs))
        print(kwargs)
        sum = 0
        for i in kwargs:
            sum += kwargs[i]
        print('total sum is ', sum)


sum_4(a=1, b=2, c=3, d=4, e=5)

print()

print(note := 'we can also pass the position arguments, but they should be before kwargs')


def sum_5(x, y, **kwargs):
    sum = x + y
    if len(kwargs):
        print(type(kwargs))
        print(kwargs)
        for i in kwargs:
            sum += kwargs[i]
        print('total sum is ', sum)


sum_5(10, 20, a=1, b=2, c=3, d=4, e=5)

print()
print('-----------------------')
print()
