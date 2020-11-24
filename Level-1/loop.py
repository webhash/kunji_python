# this is a comment 
# print statement default end character is new lines
print("Hello World!!")
# this one will print just the new line

print()
print('-----------------------')
print()
print(someobject := '"This is an Object"')

print(note := 'We can use "type(object)" to detect type in python')
print(type_object := type(someobject))

print(note := 'We can use "id(object)" to get memory address of object')
# hex will returns the result in hexadecimal 
print(add_obj := hex(id(someobject)))

print(note := 'We can use "len(object)" to detect length in python')
print(len_object := len(someobject))
# why does the below line works ? because len function calls/maps to __len__ method
# we shall look at this thing in more detail later
# assert can be used to ensure expected state in a program
assert len(someobject) == someobject.__len__()

print(note := 'length in python is of type')
print(type(len_object))

print()
print('-----------------------')
print()
print(note := ('below for loop shall print one value at a time of the object '
               + someobject + ' that has total length of ' + str(len_object)
               )
      )
# we create a local variable that gets new value in each iteration
# here we also change the end symbol to a specific value 
for c in someobject:
    print(c, end="<- ")

print()
print('-----------------------')
print()

print(note := 'Or we can also do following for loop')
print()

i = 0
for c in someobject:
    print(str(i) + ' ' + c, end="<-  ")
    i = i + 1
i = None
print()

print(note := 'Or we can also do following for loop')
print()

for i, c in enumerate(someobject):
    print(str(i) + ' ' + c, end="<-  ")
print()

print()
print(note := 'we can also use the while loop to get the similar result')
i = 0
while i < len_object:
    print(str(i) + ' ' + someobject[i], end="<-  ")
    i += 1
i = None
print()

print(note := 'but while loop is not same as for loop ')
print(note := 'for loop can be used on any object that is iterable')
print()
print('-----------------------')
print()

print(note := 'python has a "range" function to get ordered integer')

# default step value is 1
print(ranger := range(0, len_object))

for i in ranger:
    print(someobject[i] + ' is  at index ' + str(i))

print()
print('-----------------------')
print()

# default start is 0
print(ranger := range(len_object))

for i in ranger:
    print(someobject[i] + ' is  at index ' + str(i))

print()
print('-----------------------')
print()

print(note := 'We get a new range with step value as 2')
print(ranger := range(0, len_object, 2))

for i in ranger:
    print(someobject[i] + ' is  at index ' + str(i))

print()
print('-----------------------')
print()

print(note := 'we can have loop within loop')

for l in range(0, 2):
    # we need not to form a single string, we can pass different types to print
    # separated by the commas
    print('Level is ', l)
    for r in range(0, 2):
        print('Row number is', r)


print()
print('-----------------------')
print()

print(note := 'as many level as we want, but remember the complexity. \
the more layers of loop you have the more the time complexity')

for l in range(0, 2):
    # we need not to form a single string, we can pass different types to print
    # separated by the commas
    print('Level is ', l)
    for r in range(0, 2):
        print('Row number is', r)
        for c in range(0, 3):
            print('Col no is ', c)

print()
print('-----------------------')
print()

print(note := 'If we create a string object with same value as object')
print(string_object := str(someobject))
print(note := 'python would assign the same memory as the original object')
print(add_obj)
print(hex(id(string_object)))
# assert can be used to ensure expected state in a program
assert hex(id(string_object)) == add_obj
print()
print('-----------------------')
print()

print(note := 'Lets change the object value to ')
print(someobject := '"New Object"')
print(note := 'Now the Address also changes')
print(new_add_obj := hex(id(someobject)))
assert hex(id(string_object)) != new_add_obj
assert add_obj != new_add_obj

print()
print('-----------------------')
print()

print(note := 'Lets have quick look at string interning')
print(note := 'create two strings with same content, note how we have used underscores')

str_a = 'welcome_home'
str_b = 'welcome_home'
print(str_a)
print(hex(id(str_a)))
print(str_b)
print(hex(id(str_b)))
assert id(str_a) == id(str_b)
print(note := 'In Python all the identifiers are interned, Python will also intern string \
 literals that look like identifiers.')
print(note := 'but behavior depends on the version of python as this is internal details, \
like in python 3.9 almost every string is interned')

print()
print('-----------------------')
print()

print(note := 'Some objects can be modified i.e mutable, and some cant i.e immutable')
print(note := 'string object cant be modified, they are allocated new memory when modified')

print()
print('-----------------------')
print()
print(note := 'For example we can use upper function to convert string to uppercase')
print(note := 'python will allocate new memory for upper cased string, original string does not change')
print(string_obj_up := string_object.upper())
print(string_object)
print(note := 'new address for above string is ', hex(id(string_obj_up)))
print(note := 'which is different from ', hex(id(string_object)))
assert hex(id(string_obj_up)) != hex(id(string_object))
assert hex(id(string_object.upper())) != add_obj
print()
print(note := 'if we convert both the strings back to lowercase python will again point them to same memory location')
print(note := 'this is again the magic of interning')
assert string_object.lower() == string_obj_up.lower()
assert hex(id(string_object.lower())) == hex(id(string_object.lower()))
print()
print('-----------------------')
print()
