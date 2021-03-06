print("Hello World!!")

print()
print('-----------------------')
print()

print(note := 'python has many inbuilt higher level data structures to make life of programmer easy')

print(note := 'lets look at lists first')

print(note := 'we can create the list either by using the list() function')
some_list1 = list()
print(type(some_list1))
print(note := 'or we can use the square brackets [] to create one')
some_list2 = []
print(type(some_list2))

print(note := 'list are mutable, i.e. we can change the content of them')
print(note := 'Lets take the address of the list')
print(some_list_add1 := hex(id(some_list1)))
print(note := 'now add few items top this list')
some_list1.append('yes')
some_list1.append(1)
print(note := 'we have added different type of items to list, one is string, other is int')
print(some_list1)
print(note := 'the address of list remains the same')
print(hex(id(some_list1)))
assert some_list_add1 == hex(id(some_list1))

print()
print('-----------------------')
print()

print(
    note := 'concatenating the list would change the address as + creates a new copy of list and assign to the variable')
some_list2 = some_list1 + ['no']
print(some_list2)
print(hex(id(some_list2)))
print(some_list1)
print(some_list_add1)
assert hex(id(some_list2)) != some_list_add1

print(
    note := 'python supports a cool feature called list comprehensions, which can be used to create list one run time based on other iterables')

list_comp = [i * 2 for i in some_list1]

print(list_comp)

list_comp = [i ** 2 for i in (1, 2, 3, 4, 5, 6)]

print(list_comp)

print(note := 'we can also use conditional inside with list comprehension')
print(note := 'we shall print only the odd values')

list_comp = [i for i in list_comp if i % 2]

print(list_comp)

print()
print('-----------------------')
print()

print(note := 'what all function does list supports?')
for item in dir(some_list1):
    if not ('__' in item):
        print(item)

print()
print('-----------------------')
print()

print(note := 'lets look dict now ... my favorite data structure')
print(note := 'we can create the dict either by using the dict() function')
some_dict1 = dict()
print(type(some_dict1))
print(some_dict_add1 := hex(id(some_dict1)))
print(note := 'or we can use the curly brackets {} to create one')
some_dict2 = {}
print(type(some_dict1))
print(some_dict_add2 := hex(id(some_dict2)))

print(note := 'dict are also mutable, i.e. we can change the content of them')
some_dict1['yes'] = 0
some_dict1['no'] = 1
print(some_dict1)
print(hex(id(some_dict1)))
assert some_dict_add1 == hex(id(some_dict1))
print(note := 'again and again and yet the address will remain the same')
some_dict1['yes'] = 1
some_dict1['no'] = 0
print(some_dict1)
print(hex(id(some_dict1)))
assert some_dict_add1 == hex(id(some_dict1))

print()
print('-----------------------')
print()

print(note := 'what all function does dict supports?')
for item in dir(some_dict1):
    if not ('__' in item):
        print(item)

print()
print('-----------------------')
print()

print(note := 'lets have a look at the set')
print(note := 'sets are mutable')
print(note := 'we can create the sets either by using the set() function')
some_set1 = set()
print(some_set1)
print(type(some_set1))
print(note := 'we can also create set by using the {} brackets')
print(note := 'we we do not add some values to {} python will assume that you wanted to create an empty dict')
some_set2 = {'yes', 'no', 'maybe'}
print(some_set2)
print(type(some_set2))
assert type(some_set2) == type(some_set1)
print(
    note := 'set is not ordered , i.e. we can not be sure that when we print the value they are printed in the same order as we added them')

print()
print('-----------------------')
print()

print(note := 'what all function does set supports?')
for item in dir(some_set1):
    if not ('__' in item):
        print(item)

print()
print('-----------------------')
print()

print(note := 'now finally lets have a look at the tuples')
print(note := 'tuples are immutable like strings')
print(note := 'we can create the tuple either by using the tuple() function')
empty_tuple = tuple()
print(empty_tuple)
print(type(empty_tuple))
print(note := 'we can not change the above empty tuple, but we can point the "empty_tuple" to new tuple/data type')
print(note := 'we can create tuple by using the () brackets and values separated by comma')
some_tuple = ('yes', 'no', 'maybe')
print(some_tuple)
print(type(some_tuple))

print(note := 'we can create tuple by using the just the comma separated values')
some_tuple = 'yes', 'no', 'maybe', 'really?'
print(some_tuple)
print(type(some_tuple))
print(note := 'so for tuples , is important than ()')
print(note := 'below we shall create an int and not the tuple')
test_tuple = (1)
print(type(test_tuple))
assert type(test_tuple) != type(some_tuple)
print(note := 'if we insert the comma we shall have the tuple')
test_tuple = (1,)
print(type(test_tuple))
assert type(test_tuple) == type(some_tuple)
print(note := ' and as mentioned before we can remove the brackets too')
test_tuple = 1,
print(type(test_tuple))
assert type(test_tuple) == type(some_tuple)

print()
print('-----------------------')
print()

print(note := 'what all function does tuples supports?')
for item in dir(some_tuple):
    if not ('__' in item):
        print(item)

print()
print('-----------------------')
print()

print(
    note := 'lets have a look at the zip function that consumes two or more iterables, and generates iterables of tuple with values from each iterable passed to it')

print(list(zip([1, 2, 3, 4], ['a', 'b', 'c', 'd'], ['yes', 'no', 'maybe'])))
print([str(x) + y for x, y, in zip([1, 2, 3, 4], ['a', 'b', 'c', 'd'])])
print(note := 'as you noticed above zip produces number of pairs equal to the smallest length of list passed to it')
print()
print('-----------------------')
print()

print(note := 'list, dict, set, tuple, str are all iterable in python')
print(note := 'thus  we can use the generic for loop on them')

print(note := 'some_tuple')
for item in some_tuple:
    print(item)

print()
print(note := 'some_dict1')
for item in some_dict1:
    print(item)

print()
print(note := 'some_list1')
for item in some_list1:
    print(item)

print()
print(note := 'some_set2')
for item in some_set2:
    print(item)

print()
print('-----------------------')
print()

print()
print(note := 'and we can also use the unpacking behavior')

s, t, r, i, n, g = "string"
print(s, t, r, i, n, g)

S, E, T = {'s', 'e', 't'}
print(S, E, T)

t, u, p, l, e = ('t', 'u', 'p', 'l', 'e')
print(t, u, p, l, e)

d, i, c, t = {'d': 1, 'i': 2, 'c': 3, 't': 4}
print(d, i, c, t)

print(
    note := 'but we have to ensure that we have same number of variables as the number of item(or length) in iteratable')
print(note := 'or else we shall get ValueError ')
print(note := 'but many times we do not know the length before hand')

print()
print('-----------------------')
print()

print(
    note := 'we can use the * to let python do the magic i.e creating a list of all the remainder of values and assign it to starred variable')
print(note := 'name of this magic is unpacking')

print()
s, *tring = 'string'
print(type(s))
print(type(tring))
print(s, tring)

print()
s, *et = {'s', 'e', 't'}
print(type(s))
print(type(et))
print(s, et)

print()
print(note := 'we can also have *variable in middle , but we can have only one of them at same level')
t, *u, ple = ('t', 'u', 'p', 'l', 'e')
print(type(t))
print(type(u))
print(type(ple))
print(t, u, ple)

print()
d, *ict = {'d': 1, 'i': 2, 'c': 3, 't': 4}
print(type(d))
print(type(ict))
print(d, ict)
print(note := 'as you noticed that single * unpacks only the keys of the dict')

print()

print(note := 'as tring et, u and ict are list, below statement shall create list of list')
l = [tring, et, u, ict]
print(l)
print()

print(note := 'as python also support nested unpacking, we can have things like below')
print(
    note := 'we mentioned that we can have only one * at one level, here we can see the real example, x,y,z is inner level and can use *')
a, *b, (x, *y, z) = [1, 2, 3, 'magic']
print(a, b, x, y, z)

print()
print(note := 'we can use the * to unpack the lists')
l = [*tring, *et, *u, *ict]
print(note := 'voila')
print(l)

print()
print(note := 'we can also unpack a string into list of individual letters')
some_string = 'magic'
l = [*tring, *et, *u, *ict, *some_string]
print(l)

print()
print(note := 'we can use the unpacking to create sets too')
s1 = {'yes', 'no', 'maybe'}
s2 = {'right', 'wrong'}

S = {*s1, *s2}
print(S)
print(note := 'but as sets are not ordered data structure, do not expect any order in result')

print(note := 'remember that when we unpack a dict only the keys are returned')
d1 = {'yes': 1, 'no': 0, 'maybe': 2}
d2 = {'right': -1, 'wrong': -2}
print()

print(note := 'we get the keys and thus create  set and not a dict')
D = {*d1, *d2}
print(D)
print(type(D))
print()

print()
print(note := 'if you want to get both key,values from the dict we have to use double * i.e. **')
D = {**d1, **d2}
print(D)
print(type(D))

print()
print('-----------------------')
print()
