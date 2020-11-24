print("Hello World!!")

print()
print('-----------------------')
print()

print(note := "Lets first have a look at the global and local scopes before we go into closures")
print(note := "scope of the variable is determined by where it is defined")
this_is_global = "I'm global"


def some_func():
    this_is_local = "I'm Local"
    print(this_is_local)
    print(this_is_global)


some_func()
print(note := 'Above function access the global variable as it was not found inside its own code block')

print()
print('-----------------------')
print()


def some_func_2():
    this_is_local = "I'm Local"
    this_is_global = "I'm not global"
    print(this_is_local)
    print(this_is_global)


some_func_2()
print(
    note := "In the above function, we created a local variable with the same name as the global variable, \
    and thus we shall see the local values printed")

print(note := "the value of the global variable remains unchanged")
print(this_is_global)

print()
print('-----------------------')
print()

print(note := "If we want to modify the global variable within the local context, python provides the global keyword")

this_is_new_global = "I am something"


def some_func_3():
    global this_is_global
    global this_is_new_global
    this_is_local = "I'm Local"
    this_is_global = "global shall be changed"
    this_is_new_global = "I'm global now"
    print(this_is_local)
    print(this_is_global)
    print(this_is_new_global)


some_func_3()

print()
print('-----------------------')
print()

print(note := "now the value of the global variable also changes")
print(this_is_global)
print(
    note := "in the above function we also created a new global variable which was not defined before the function call")
print(
    note := "magic of global keyword is that it creates this new variable in global scope and can be referenced by others later, if required")
print(this_is_new_global)

print(note := "del command can be used to delete a variable")
del this_is_global

print()
print('-----------------------')
print()

print(note := "we can have function defined within functions, called nested function")
print(
    note := "in those scenarios python search for the outer function for a variable referenced given its not available in current context")
print(note := "and will throw error if nothing is found till the main level/ global scope")
print(
    note := "if we assign value to the within inner function, to a variable defined in outer function then the outer value will be masked")


def function_out():
    local_out = 'im local to function out'
    out = "this is out"

    def function_in():
        print("we are inside the function_in, and can access the local_out")
        print(local_out)
        out = "but this is in"
        print(out)

    function_in()
    print(out)


function_out()

print()
print('-----------------------')
print()

print(
    note := "python also has the keyword nonlocal for the scenarios when we want to change the variable in outer scope")


def function_out_2():
    local_out = 'im local to function out'
    out = "this is out"

    def function_in():
        print("we are inside the function_in, and can access the local_out")
        print(local_out)
        nonlocal out
        out = "this is new out"
        print(out)

    function_in()
    print(out)


function_out_2()

print()
print('-----------------------')
print()

print(note := "lets mix nonlocal and global together")

new_global = "i'm global"


def function_out_3():
    new_global = "this is not global, global variable got masked"
    out = "this is out variable"
    print("we are inside out function")
    print("new_global is : ", new_global)

    def function_in():
        nonlocal out
        out = "this is now new out variable"
        print("We are inside in function")

        def function_in_in():
            global new_global
            new_global = "this will be the new global value"
            print("we are inside inner most function")

        print(new_global)
        function_in_in()
        print(out)

    print(new_global)
    function_in()
    print(new_global)


function_out_3()

print()
print('-----------------------')
print()

print(note := "Now we will look at the closures")
print(note := "we have to look at the concept of cell")
print()

print(note := "lets create a function that contains a variable and another inner function")
print(note := "inner function access the variable defined in out function")
print()


def out():
    versions = ['v1.0', 'v1.2']
    print("we are in out")
    print(hex(id(versions)))

    def inside():
        print("we are in inside")
        print(hex(id(versions)))
        print(versions)

    print("address of the inside function is ", hex(id(inside)))
    return inside


print("address of the out function is ", hex(id(out)))
r = out()
print(note := "Cell objects are used to implement variables referenced by multiple scopes.")
print(note := "For each such variable, a cell object is created to store the value")
print(note := 'cell refers to the address of the versions in outer variable')
print(r.__closure__)
print(note := 'we can see the versions in the co_freevars portion of the __code__')
print(r.__code__.co_freevars)
r()

print()
print('-----------------------')
print()

print(
    note := "as we can have a common variable access by multiple inner function, they will basically use the same cell")


def out_1():
    version = 0

    def inc_v_1():
        nonlocal version
        version += 1
        return version

    def inc_v_2():
        nonlocal version
        version += 2
        return version

    return inc_v_1, inc_v_2


a, b = out_1()
print(
    note := "we shall see the same closure information for both the inner function returned as they access the same variable")
print(a.__closure__)
print(a.__code__.co_freevars)

print(b.__closure__)
print(b.__code__.co_freevars)

print(a())
print(b())
print(a())
print(b())

print()
print('-----------------------')
print()

print(note := "lets make a more complex scenario with closures")

print(note := "we define a counter function that consumes a function")


def counter(fn):
    count = 0

    # fn is also local to inner function
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('Function ', fn.__name__, ' called ', count, ' times')
        return fn(*args, **kwargs)

    return inner


def multiply(x, y=1):
    return x * y


print(note := 'the multiply function has below address')
print(hex(id(multiply)))
print(note := 'original multiply function just prints the results')
print(multiply(1, 2))

print(note := 'after we pass the multiply to counter, we shall have a new multiply')
multiply = counter(multiply)
print(hex(id(multiply)))
print(note := 'new  multiply function prints the results and also the counter')
print(multiply(1, 2))

print()
print('-----------------------')
print()

print(note := "now lets quickly have a look at decorators")
print(note := "we have already scene decorators in classes, like @classmethod, @staticmethod")

print(note := 'the way we used multiply = counter(multiply) to apply counter to the multiple function')
print(note := 'python supports the @ option to do that same, beautifully')


@counter
def add(a, b=0):
    return a + b


print(note := 'now the add function itself has the counter feature enabled on it')

print(add(1, 2))

print()
print('-----------------------')
print()
